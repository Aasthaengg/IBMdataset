import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k = map(int,readline().split())
ans = 0
if k == 0:
    print(n**2)
    exit()
for b in range(1,n+1):
    if b <= k:
        continue
    #a=nとして考えて良い。
    ans += n//b*(b-k)
    ans += max(0,n%b-(k-1))

print(ans)


