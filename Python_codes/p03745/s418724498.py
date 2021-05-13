import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
l = []
prev = None
for i in range(n):
    if prev!=a[i]:
        l.append(a[i])
    prev = a[i]
        
if len(l)==1:
    ans = 1
else:
    m = len(l)
    prev = None
    ans = 0
    for i in range(m-1):
        s = l[i]<l[i+1]
        if prev is None:
            prev = s
        elif prev!=s:
            ans += 1
            prev = None
    ans += 1
print(ans)