N = int(input())
lls = []
rls = []
sels = []
for _ in range(N):
    x,l = map(int, input().split())
    lls.append(x-l)
    rls.append(x+l)
    sels.append([x-l,x+l])

sels = sorted(sels,key=lambda x:x[1])

start = -float('inf')

ans = 0
for item in sels:
    if start <= item[0]:
        ans += 1
        start = item[1]

print(ans)
