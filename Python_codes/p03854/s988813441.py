s=input()
s=s[::-1]
f=0
l=['dream' ,'dreamer', 'erase','eraser']
l=[c[::-1] for c in l]
while(f==0):
    if(s[:7] in l):
        s=s[7:]
    elif(s[:6] in l):
        s=s[6:]
    elif(s[:5] in l):
        s=s[5:]
    else:
        f=1
if(len(s)==0):
    print("YES")
else:
    print("NO")
