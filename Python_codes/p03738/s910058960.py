def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
a = ii()
b = ii()

if a > b:
    print('GREATER')
elif a == b:
    print('EQUAL')
else:
    print('LESS')