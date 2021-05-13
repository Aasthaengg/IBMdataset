#S= str(input())
#T= str(input())
#N = int(input())
A,B,M= map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C=10**6
for i in range(M):
    x,y,c= map(int,input().split())
    cost = A[x-1] + B[y-1] - c
    if cost<=C:
        C=cost
if min(A)+min(B)<=C:
    C=min(A)+min(B)
print(C)
