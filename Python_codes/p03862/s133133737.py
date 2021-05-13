import sys
def LI():
    return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,x = LI()
a = LI()

ans = 0

# 左から2番目以降貪欲に

if a[0] > x:
    ans += a[0]-x
    a[0] = x

for i in range(1,N):
    if a[i]+a[i-1] > x:
        ans += a[i]+a[i-1]-x
        a[i] -= a[i]+a[i-1]-x

print(ans)