N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

mn = 10000000
ans = 0
for i in range(N):
    now = T - H[i] * 0.006
    if abs(now - A) <= mn:
        mn = abs(now - A)
        ans = i
print(ans + 1)
