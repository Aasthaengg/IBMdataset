n = int(input())
T = list(map(int, input().split()))
m = int(input())
PX = []
for i in range(m):
    p, x = map(int, input().split())
    p -= 1
    PX.append((p, x))

S = sum(T)
for i in range(m):
    p, x = PX[i]
    ans = S - T[p] + x
    print(ans)
