s=list(input())
c=len(s)+10
n=len(s)
f=-len(s)
for i in range(len(s)):
    if s[n-1-i]=='F':
        f=n-1-i
        break
for i in range(n):
    if s[i]=="C":
        c=i
        break
if c<f:
    print('Yes')
else:
    print('No')