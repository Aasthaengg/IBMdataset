n, k, q = list(map(int, input().split()))
pp = [0] * n
for _ in range(q):
    a = int(input())
    pp[a - 1] += 1
for i in range(n):
    print('Yes' if k - (q - pp[i]) > 0 else 'No')