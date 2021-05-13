N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
res = 10 ** 6
idx = 0
for i, h in enumerate(H):
    tmp = abs(A - T + h * 0.006)
    if tmp < res:
        res = tmp
        idx = i + 1
print(idx)