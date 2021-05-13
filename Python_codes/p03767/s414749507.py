n = int(input())
A = list(map(int,input().split()))
A.sort()
B = A[n:n*2]
C = A[-2:-2-n*2:-2]
D = A[1:n*3+1:3]

ans = max(sum(B), sum(C), sum(D))
print(ans)