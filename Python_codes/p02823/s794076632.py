def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n,a,b = iim()

if (a%2)^(b%2):
    num = min(a-1,n-b)+1
    print((b-a)//2+num)
else:
    print((b-a)//2)