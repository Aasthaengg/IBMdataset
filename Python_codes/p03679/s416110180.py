def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

x,a,b = iim()

if b - a <= 0:
    print('delicious')
elif b - a <= x:
    print('safe')
else:
    print('dangerous')