from collections import Counter

# input
N = int(input())
A = Counter(list(map(int, input().split())))

# check
res = 0
for n, c in A.most_common():
    if c >= n:
        res += c - n
    else:
        res += c

print(res)