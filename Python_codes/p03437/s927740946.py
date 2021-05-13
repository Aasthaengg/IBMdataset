def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

x,y = iim()

if y == 1 or x%y == 0:
    print(-1)
else:
    print(x*(y-1))