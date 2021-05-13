import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,x = map(int,readline().split())
lst1 = list(map(int,readline().split()))

lst1.sort()

i = 0
ans = 0
while i < n:
    if lst1[i] > x:
        break
    x -= lst1[i]
    ans += 1
    i += 1

if i == n:
    if x == 0:
        print(ans)
    else:
        print(ans-1)
else:
    print(ans)