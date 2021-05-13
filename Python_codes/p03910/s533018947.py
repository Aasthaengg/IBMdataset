import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())

res = 0
ret = 0
for i in range(1,n+1):
    res += i
    if res >= n:
        ret = i
        break

ans = []
while n:
    if n-ret < 0:
        ret -= 1
    else:
        ans.append(ret)
        n -= ret
        ret -= 1

for i in ans:
    print(i)