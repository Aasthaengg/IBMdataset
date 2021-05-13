N, X = map(int, input().split())
L = list(map(int, input().split()))

jump = [0]
num = 0
for i in range(N):
    num += L[i]
    jump.append(num)

ans = 0
for i in jump:
    if i <= X:
        ans += 1
print(ans)
