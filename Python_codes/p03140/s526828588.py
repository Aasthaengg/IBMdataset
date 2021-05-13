def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = list(input())
B = list(input())
C = list(input())

ans = 0
for i in range(n):
    num = len(set([A[i],B[i],C[i]]))
    if num == 2:
        ans += 1
    elif num == 3:
        ans += 2
print(ans)