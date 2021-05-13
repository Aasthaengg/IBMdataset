# AGC 006: A – Prefix and Suffix
N = int(input())
s, t = [input() for _ in range(2)]

common = 0

for i in range(N):
    if s[(N - i - 1):N] == t[0:i + 1]:
        common = len(t[0:i + 1])

print(N * 2 - common)