def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))

a,b,c = iim()

if b-a == c-b:
    print('YES')
else:
    print('NO')