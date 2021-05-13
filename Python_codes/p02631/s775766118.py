N = int(input())
A = list(map(int,input().split()))
B = A[0]
for i in range(1, N):
    B = B ^ A[i]
#print(B)
for j in A:
    print(B ^ j)