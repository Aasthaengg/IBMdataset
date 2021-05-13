def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,a,b = iim()
if n > 1:
    print(max((n-2)*(b-a)+1,0))
else:
    if a==b:
        print(1)
    else:
        print(0)