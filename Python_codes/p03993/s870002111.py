def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
cnt = 0
for i in range(n):
#    print(i,A[i],A[A[i] - 1]-1)
    if i == A[A[i] - 1] - 1:
        cnt += 1
print(cnt // 2)
