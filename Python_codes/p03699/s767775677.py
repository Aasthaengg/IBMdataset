import itertools
n = int(input())
sl = []
for _ in range(n):
    sl.append(int(input()))

if sum(sl) % 10 != 0:
    print(sum(sl))
    exit()

ans = 0
for v in itertools.combinations(sl,n-1):
   if sum(v) % 10 != 0:
    ans = max(ans, sum(v))
print(ans)