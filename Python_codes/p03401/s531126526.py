n = int(input())

A = list(map(int,input().split()))
A.append(0)

S = abs(A[0])
for i in range(1,n+1):
    S +=abs(A[i]-A[i-1])

for i in range(n):
    if i == 0:
        s = S + abs(A[1]-0) - (abs(0-A[0])+abs(A[0]-A[1]))
        print(s)
    else:
        s = S + abs(A[i+1]-A[i-1]) - (abs(A[i-1]-A[i])+abs(A[i]-A[i+1]))
        print(s)