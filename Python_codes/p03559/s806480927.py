import bisect


I = lambda: map(int, input().split())
N = int(input())
A = list(I())
B = list(I())
C = list(I())
B.sort()
C.sort()

s = [0] * (N + 1)
for i, bi in enumerate(B):
    s[i + 1] = s[i] + N - bisect.bisect_right(C, bi)

print(sum(s[N] - s[bisect.bisect_right(B, ai)] for ai in A))