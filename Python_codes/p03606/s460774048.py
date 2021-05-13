def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
ans = 0
for i in range(n):
    l,r = iim()
    ans += r-l+1
print(ans)