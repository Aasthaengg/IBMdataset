N = int(input())
A = list(map(int, input().split()))
B = [0] * N
ans = []

for i in range(N, 0, -1):
  j = 1
  cnt = 0

  while i * j <= N:
    cnt += B[(i*j) - 1]
    j += 1
  
  cnt %= 2
  B[i-1] = A[i-1] ^ cnt #排他的論理和XOR
  
  if B[i-1] == 1:
    ans.append(i)

print(sum(B))
print(*ans)