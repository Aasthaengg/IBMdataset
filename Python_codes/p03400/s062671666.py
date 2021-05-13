N = int(input())
D,X = map(int,input().split())
A = [int(input()) for _ in range(N)]
for i in range(N):
    a = A[i]
    X += (D-1)//a+1
print(X)