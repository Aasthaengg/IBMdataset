def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,h,w = iim()
ans = 0
for i in range(n):
    a,b = iim()
    if a >= h and b >= w:
        ans += 1
print(ans)