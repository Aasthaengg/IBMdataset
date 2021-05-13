n = int(input())
l=[[] for _ in range(n)]
for i in range(n):
    a,b = input().split()
    b=int(b)
    l[i].append(a)
    l[i].append(b)

c=input()
memo=0
ans=0
for i in range(n):
    if memo==1:
        ans+=l[i][1]
    if l[i][0]==c:
        memo=1

print(ans)