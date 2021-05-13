s = input()
l = len(s)
t = [0]*l
c=0
ch=0
for i in range(l):
    if s[l-1-i]=='C' and c == 0:
        c=1
    elif s[l-i-1]=='B' and c == 1:
        c=0
        ch+=1
    elif s[l-i-1]=='A' and c == 1:
        c=0
        ch = 0
    elif s[l-i-1]=='A':
        c=0
    elif s[l-i-1]=='C' and c==1:
        ch=0
        c=1
    else:
        ch=0
        c=0
    t[l-i-1]=ch
ans = 0
for i in range(l):
    if s[i]=='A':
        ans += t[i]
print(ans)
