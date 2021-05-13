n = int(input())
A = list(map(int, input().split()))
if n % 2 == 0:
    l = n ** 2
else:
    l = (n - 1) * (n + 1)
if sum(A) == l // 2:
    print(2 ** (n // 2) % (10 ** 9 + 7))
else:
    print(0)
