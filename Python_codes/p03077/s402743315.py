def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n = ii()
l = []
for i in range(5):
    l.append(ii())

print((n+min(l)-1)//min(l)+4)