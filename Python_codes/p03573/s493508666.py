def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
a,b,c = iim()

if a == b:
    print(c)
else:
    if a == c:
        print(b)
    else:
        print(a)