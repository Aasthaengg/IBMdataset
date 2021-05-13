import sys
input = lambda: sys.stdin.buffer.readline()

n = int(input())
a = list(map(int, input().split()))
a.sort()

m = 10**6+10
d = [False] * (m+1)
ans = 0
for i in range(n):
    same = (i > 0 and a[i] == a[i-1]) or (i < (n-1) and a[i] == a[i+1])
    x = a[i]
    if not d[x] and not same: ans += 1
    
    if (i > 0 and a[i] == a[i-1]): continue
    for j in range(x, m+1, x):
        d[j] = True
    
print(ans)
