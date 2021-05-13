N = int(input())
A = [0]+list(map(int,input().split()))+[0]
B = [0]
b = 0
for i in range(1,N+2):
    B.append(B[i-1]+abs(b-A[i]))
    b = A[i]
for i in range(1,N+1):
    x,y = B[i]-B[i-1],B[i+1]-B[i]
    z = abs(A[i+1]-A[i-1])
    print(B[N+1]-x-y+z)