N, A, B = map(int, input().split())
X = [int(_) for _ in input().split()]
ans = 0
for i in range(1, N):
    walk = (X[i]-X[i-1])*A
    teleport = B
    if walk < teleport:
        ans += walk
    else:
        ans += teleport

print(ans)