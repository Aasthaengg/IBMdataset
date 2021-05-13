# AGC 031: A – Colorful Subsequence
N = int(input())
S = input()
s = set(S)
s_count = [S.count(c) + 1 for c in s]

tmp = 1
for i in s_count:
    tmp *= i

print((tmp - 1) % (10 ** 9 + 7))