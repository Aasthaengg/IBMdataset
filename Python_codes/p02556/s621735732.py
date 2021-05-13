def LI():
    return list(map(int, input().split()))


pu = []
mi = []
N = int(input())
for _ in range(N):
    x, y = LI()
    pu.append(x+y)
    mi.append(x-y)
P = max(pu)
p = min(pu)
M = max(mi)
m = min(mi)
print(max(P-p, M-m))
