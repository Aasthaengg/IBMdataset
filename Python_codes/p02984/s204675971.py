n = int(input())
A = list(map(int,input().split()))
x = A[0]
for i in range(1,n):
    if i % 2 == 0:
        x -= A[i]
    else:
        x += A[i]
x = x//2
ans = [2*(A[0]-x)]
for i in range(1,n):
    ans.append(2*x)
    x = A[i]-x
print(" ".join(map(str,ans)))