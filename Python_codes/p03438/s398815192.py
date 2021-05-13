import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = sum(b) - sum(a)
m = [(max(a[i], b[i])+(a[i]<b[i] and (b[i]-a[i])%2==1)) for i in range(n)]
if k>=0 and sum(a)+2*k>=sum(m) and sum(b)+k>=sum(m):
    ans = "Yes"
else:
    ans = "No"
print(ans)