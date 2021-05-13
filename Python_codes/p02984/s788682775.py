N = int(input())
A = list(map(int, input().split()))
num = 0
Ans = [0] * N
for a in A:
    num = (a - num // 2) * 2

num //= 2
for i, a in enumerate(A):
    Ans[i] = str(num)
    num = (a - num // 2) * 2

print(' '.join(Ans))
