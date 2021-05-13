n = int(input())
A = list(map(int,input().split()))
for i in range(1,n+1):
    A[i-1] = A[i-1]-i
A.sort()
flag = True
if n % 2 == 1:
    b = A[(n-1)//2]
else:
    if A[n//2] == A[n//2-1]:
        b = A[n//2]
    else:
        flag = False
if flag:
    ans = 0
    for i in A:
        ans += abs(i-b)
    print(ans)
else:
    ans1=0
    ans2=0
    for i in A:
        ans1 += abs(i-A[n//2])
        ans2 += abs(i-A[n//2-1])
    print(min(ans1,ans2))