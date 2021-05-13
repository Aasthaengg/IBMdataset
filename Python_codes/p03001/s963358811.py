def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

w,h,x,y = iim()
area = w*h/2

f = 1 if w/2 == x and h/2 == y else 0
print(area,f)