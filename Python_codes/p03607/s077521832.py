import collections
N = int(input())
A = [int(input()) for i in range(N)]
ans = 0
dict = collections.Counter(A)

for a, b in dict.items():
    if b % 2 != 0:
        ans += 1
print(ans)