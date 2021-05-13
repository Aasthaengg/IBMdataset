import sys
n = int(input())
a = [ 2*int(i) for i in sys.stdin.readline().split()]
ans = [0 for i in range(n)]
for i in range(1, n):
    ans[i] = a[i-1] - ans[i-1]
ans[0] = (a[n-1] - ans[n-1])//2
for i in range(1, n):
    ans[i] +=  ans[0]*(-1)**(i%2)
print(" ".join(map(str, ans)))
