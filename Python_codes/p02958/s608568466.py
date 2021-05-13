n=int(input())
p=list(map(int,input().split()))
s=sorted(p)
c=0
for i in range(n):
    if s[i]!=p[i]:
        c+=1
if c>2:
    print('NO')
else:
    print('YES')