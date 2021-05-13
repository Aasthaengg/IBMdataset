s=input()
a,b,c=0,0,0

for i in range(len(s)):
    if s[i]=='a':
        a+=1
    elif s[i]=='b':
        b+=1
    else :
        c+=1

ans = (abs(a-b) <2) and (abs(c-b)<2) and (abs(c-a)<2)
print( "YES" if ans else "NO") 