import collections

n = int(input())
a = tuple(map(int, input().split()))

m = collections.Counter(a)

# n: odd  ->  0, 2, ..., n-1
# n: even ->  1, 3, ..., n-1

if n % 2 == 0:
    mm = {2*i+1: 2 for i in range(0, n//2)}
else:
    mm = {2*i: 2 for i in range(0, n//2 + 1)}
    mm[0] = 1


for i in m:
    if i not in mm or m[i] != mm[i]:
        print(0)
        exit()

for i in mm:
    if i not in m or mm[i] != mm[i]:
        print(0)
        exit()

r = 10**9 + 7
ans = 1
for _ in range(n//2):
    ans = (ans * 2) % r

print(ans)