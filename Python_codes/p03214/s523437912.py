def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))
n = ii()
A = iil()
mean = sum(A)/n
diff = max(A)
ans = 0
for i in range(n):
    if abs(A[i] - mean) < diff:
        ans = i
        diff = abs(A[i] - mean)
print(ans)