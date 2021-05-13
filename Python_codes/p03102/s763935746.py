N, M, C = map(int, input().split())
B = list(map(int, input().split()))
ans = 0
for i in range(N):
    A = list(map(int, input().split()))
    temp = 0
    for a, b in zip(A, B):
        temp += a * b
    temp += C
    if temp > 0:
        ans += 1
print(ans)