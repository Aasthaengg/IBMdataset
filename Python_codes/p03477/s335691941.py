def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
a,b,c,d = iim()
if a+b < c+d:
    print('Right')
elif a+b > c+d:
    print('Left')
else:
    print('Balanced')