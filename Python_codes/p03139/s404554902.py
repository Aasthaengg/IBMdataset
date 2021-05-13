def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

n,a,b = iim()
print(min(a,b),max(0,a+b-n))