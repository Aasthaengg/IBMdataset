def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

r,g,b,n = iim()
ans = 0
for i in range(n//r+1):
    for j in range(n//g+1):
        num = n-i*r-j*g
        if num%b == 0 and num//b >= 0:
#            print(i,j,num//b)
            ans += 1
print(ans)