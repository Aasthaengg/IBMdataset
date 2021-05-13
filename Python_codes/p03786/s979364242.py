N = int(input())
A = list(map(int, input().split()))
A.sort()
dp, S = 0, 0
for i, a in enumerate(A):
    if S*2 < a:
        dp = i
    S += a
print(N-dp)