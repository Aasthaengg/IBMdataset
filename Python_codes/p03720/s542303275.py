n,m =map(int, input().split())
l = []

for _ in range(m):
    for i in map(int, input().split()):
        l.append(i)

ans = []
        
for i in range(1,n+1):
    ans.append(l.count(i))

for i in ans:
    print(i)