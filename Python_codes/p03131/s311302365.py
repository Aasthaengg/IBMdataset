def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

k,a,b = iim()
if k == 1 or b-a <= 2:
    print(1+k)
else:
    rem = k-a-1
    if rem%2 == 0:
        print(b+(b-a)*(rem//2))
    else:
        print(b+(b-a)*(rem//2)+1)
