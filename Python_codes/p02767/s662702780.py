N = int(input())
X = list(map(int, input().split()))

ans = []
for p in range(100+1):
    phys = 0
    for x in X:
        phys += (x-p)**2
    ans.append(phys)

print(min(ans))
