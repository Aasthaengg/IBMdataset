N = int(input())
A = list(map(int, input().split()))

tx = 0
for a in A:
  tx = tx ^ a

#print(tx)

ans = [""] * N
for i in range(N):
  ans[i] = str(tx ^ A[i])
  
print(" ".join(ans))