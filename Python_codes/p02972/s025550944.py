N = int(input())
A = list(map(int, input().split()))
B = [0] * N
ans = []

for i in range(N, 0, -1):
  cnt = sum(B[(i-1)::i])%2
  B[i-1] = A[i-1] ^ cnt
  if B[i-1]:
    ans.append(i)

print(sum(B))
print(*ans)