N = int(input())
p = []
for _ in range(N):
    p.append(int(input()))
p = sorted(p)
print(sum(p)-p[-1]//2)