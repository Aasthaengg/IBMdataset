def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a,b = iim()

if b%a == 0:
    print(a+b)
else:
    print(b-a)