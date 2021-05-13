I = lambda: map(int, input().split())
nums = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
minf = -float('inf')
n, _ = I()
*A, = sorted(I(), reverse = True)
digs = [0]*(n+1)+[-1]*9
for i in range(1, n+1):
    d = []
    for a in A :
        before = i-nums[a]
        d.append(minf if before < 0 else digs[before]+1)
    digs[i] = max(d)
ans = []
while n > 0:
    for a in A:
        if digs[n-nums[a]] == digs[n]-1:
            ans.append(a)
            n -= nums[a]
            break
print(*ans, sep = '')