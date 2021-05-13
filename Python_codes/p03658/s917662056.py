def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
ans = 0
n,k = iim()
L = sorted(iil(),reverse=True)
for i in range(k):
    ans += L[i]

print(ans)