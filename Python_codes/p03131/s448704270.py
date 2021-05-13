K, A, B = map(int, input().split())
if A >= B - 1 or K <= A - 1:
    print(1 + K)
else:
    r = K - (A - 1)
    print(r // 2 * (B - A) + A + r % 2)