N,M = map(int, input().split())
sels = []
for _ in range(M):
    a,b = map(int, input().split())
    sels.append([a,b])

sels = sorted(sels, key = lambda x:x[1])
start = sels[0][0]
end = sels[0][1]
ans = 1

for item in sels:
    if end <= item[0]:
        start = item[0]
        end = item[1]
        ans += 1

print(ans)
