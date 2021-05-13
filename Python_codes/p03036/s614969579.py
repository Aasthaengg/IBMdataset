def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
r,d,x=iim()

for i in range(10):
    ans = x*r-d
    print(ans)
    x = ans