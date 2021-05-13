N = int(input())
A =list(map(int,input().split()))

Ans = []
pre = -10**9
maxi = A.index(max(A))
mini= A.index(min(A))

if abs(A[maxi]) > abs(A[mini]):
    for i in range(N):
        if i != maxi:
            Ans.append([maxi+1,i+1])
    for i in range(1,N):
        Ans.append([i,i+1])
else:
    for i in range(N):
        if i != mini:
            Ans.append([mini+1,i+1])
    for i in range(N-1,0,-1):
        Ans.append([i+1,i])
print(len(Ans))
for ans in Ans:
    print(*ans, sep = " ")