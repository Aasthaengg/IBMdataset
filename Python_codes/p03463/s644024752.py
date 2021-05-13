def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
n,a,b = iim()
if (b-a)%2 == 0:
    if b-a == 1:
        print('Borys')
    else:
        print('Alice')
else:
    print('Borys')