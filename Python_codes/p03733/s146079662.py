def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,t = iim()
T = iil()

ans = t
for i in range(1,n):
    ans += min(T[i]-T[i-1],t)

print(ans)