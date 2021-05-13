N = int(input())
A = [0]+list(map(int, input().split()))+[0]
res = 0
for i in range(1,N+2):
    res += abs(A[i]-A[i-1])
for i in range(1,N+1):
    print(res - abs(A[i+1]-A[i]) - abs(A[i]-A[i-1]) + abs(A[i+1]-A[i-1]))