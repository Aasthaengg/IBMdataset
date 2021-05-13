import sys
n = int(input())
a = [ 2*int(i) for i in sys.stdin.readline().split()]
f = (sum(a) - 2* sum(a[1::2]))//2
ans = [f] + [0 for i in range(n-1)]
for i in range(n-1):
    ans[i+1] =  a[i] - ans[i]
print(" ".join(map(str, ans)))
