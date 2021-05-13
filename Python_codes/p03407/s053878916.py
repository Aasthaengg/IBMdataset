def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,b,c =iim()
if a+b < c:
    print('No')
else:
    print('Yes')