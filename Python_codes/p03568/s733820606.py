def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
odd = 1
for i in A:
    if i%2 == 0:
        odd *= 2
    else:
        odd *= 1
print(3**n - odd)