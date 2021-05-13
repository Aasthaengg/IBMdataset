N = int(input())
A = list(map(int,input().split()))
A.insert(0,0)
A.append(0)
ans = []
n = len(A)
S = 0
for i in range(1,n):
    S += abs(A[i]-A[i-1])

for i in range(1,n-1):
    sum = S + abs(A[i+1]-A[i-1])-abs(A[i-1]-A[i])-abs(A[i]-A[i+1])
    ans.append(sum)

for i in ans:
    print(i)