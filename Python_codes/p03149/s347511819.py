def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
A = sorted(iil())
if A == [1,4,7,9]:
    print('YES')
else:
    print('NO')