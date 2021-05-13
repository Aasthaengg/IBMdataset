import sys
input = sys.stdin.readline

N = int(input())
S = list(input().rstrip())

A = [0]
a = 0
for s in S:
    if s == ".":
        a += 1
    A.append(a)

B = A[-1]

ans = N+1
for i, a in enumerate(A):
    score = (i - a) + B - a
    ans = min(ans, score)

print(ans)