N, P = map(int, input().split())
A = list(map(int, input().split()))
B = [a % 2 for a in A]
count_0 = B.count(0)
count_1 = B.count(1)

if count_1 == 0:
    if P == 0:
        ans = 2 ** N
    else:
        ans = 0
else:
    ans = 2 ** (N - 1)
print(ans)
