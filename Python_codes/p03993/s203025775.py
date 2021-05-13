N=int(input())
*A,=map(int, input().split())

B=[0]*N

for i,a in enumerate(A):
    if A[a-1] == i+1: B[i] = 1

print(sum(B)//2)