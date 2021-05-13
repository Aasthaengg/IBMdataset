def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,k =iim()
if n%2 == 0:
    if k <= n//2:
        print('YES')
    else:
        print('NO')
elif k <= (n-1)//2+1:
    print('YES')
else:
    print('NO')