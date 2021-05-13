def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

a,op,b = ism()
if op == '+':
    print(int(a)+int(b))
else:
    print(int(a)-int(b))