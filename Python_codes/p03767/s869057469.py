import sys
n = int(sys.stdin.readline())
a = [int(s) for s in sys.stdin.readline().rstrip("\n").split()]
a.sort(reverse=True)
ans = 0
for i in range(n):
    ans += a[2*i+1]
print(ans)