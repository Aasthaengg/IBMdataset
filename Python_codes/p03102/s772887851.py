N, M, C = map(int, input().split())
B = list(map(int, input().split()))
res = 0
for _ in range(N):
    A = list(map(int, input().split()))
    tmp = sum(a * b for a, b in zip(A, B)) + C
    if tmp > 0:
        res += 1
print(res)