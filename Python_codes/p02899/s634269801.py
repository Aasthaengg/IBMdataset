N = int(input())
A = list(map(int,input().split()))
B = [(A[i],i+1) for i in range(N)]
B.sort()
ans = []
for i in range(N):
  ans.append(B[i][1])
print(*ans)