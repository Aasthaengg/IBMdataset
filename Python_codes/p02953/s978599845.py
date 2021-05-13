# 問題：https://atcoder.jp/contests/abc136/tasks/abc136_b

N = int(input())
H = list(map(int, input().strip().split()))

enable_non_decrease = True

for i in range(N-1):
    j = N - 1 - i
    if H[j-1] > H[j]:
        H[j-1] -= 1
    if H[j-1] > H[j]:
        enable_non_decrease = False
        break

if enable_non_decrease:
    print('Yes')
else:
    print('No')

