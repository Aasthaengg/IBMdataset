N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
out = "No"
SBA = sum(B)-sum(A)
if SBA>=0:
    cnt = 0
    for i in range(N):
        if A[i]<B[i]:
            cnt += (B[i]-A[i]+1)//2
    if cnt<=SBA:
        out = "Yes"
print(out)