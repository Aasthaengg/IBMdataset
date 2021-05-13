q = int(input())

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n != 1

def main(n):
    return 1 if is_prime(n) and is_prime((n + 1) // 2) else 0

MAX = 10 ** 5 + 100
A = [main(i) for i in range(MAX)]
# 累積和
acc = [0] * (MAX + 1)
for i in range(MAX):
    acc[i + 1] = acc[i] + A[i]

for i in range(q):
    l, r = map(int, input().split())
    # [l, r] なので r + 1 にする
    print(acc[r + 1] - acc[l])