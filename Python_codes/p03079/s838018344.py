def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

A = set(iil())
if len(A) == 1:
    print('Yes')
else:
    print('No')


