from collections import Counter

N = int(input())
S = input()

cnter = Counter(S)
alpha = set(cnter)

ans = 1

for i in alpha:
    ans *= (cnter[i] + 1)

print((ans - 1) % (10 ** 9 + 7))