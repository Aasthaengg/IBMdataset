N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

temp = 10**5
ans = 0
for i in range(N):
    t = T - H[i] * 0.006
    if abs(t - A) < temp:
        temp = abs(t - A)
        ans = i + 1
print(ans)
