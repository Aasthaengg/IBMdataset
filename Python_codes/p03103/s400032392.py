N, M = [int(n) for n in input().split()]
A = []
for i in range(N):
    a, b = [int(n) for n in input().split()]
    A.append((a,b))
SA = sorted(A)
ans = 0
while True:
    sa = SA.pop(0)
    if sa[1] < M:
        ans += sa[0]*sa[1]
        M -= sa[1]
    else:
        ans += sa[0] * M
        break
print(ans)
