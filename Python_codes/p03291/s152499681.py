import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)
mod = 10**9 + 7
cnt = 0
A = B = C = 0
for c in S:
    if c == 'A':
        A += pow(3, cnt, mod)
    if c == 'B':
        B += A
    if c == 'C':
        C += B
    if c == '?':
        C = C * 3 + B
        B = B * 3 + A
        A = A * 3 + pow(3, cnt, mod)
        cnt += 1
    A %= mod
    B %= mod
    C %= mod
print(C)