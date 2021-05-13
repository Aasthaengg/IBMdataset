def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

w,a,b = iim()

if abs(a-b) <= w:
    print(0)
else:
    print(abs(a-b)-w)