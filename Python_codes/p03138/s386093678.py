N, K = map(int, input().split())
A = list(map(int, input().split()))

L = len(bin(max(max(A), K))[2:])
B = list(map(lambda x: "0"*(L-len(bin(x)[2:]))+bin(x)[2:], A))
#print(B)

answer = 0
for i in range(L):
  cnt = 0
  for j in range(N):
    if B[j][i] == "0":
      cnt += 1
  if cnt > N - cnt and 2**(L-i-1) <= K:
    K -= 2**(L-i-1)
    answer += 2**(L-i-1) * cnt
  else:
    K -= 0
    answer += 2**(L-i-1) * (N - cnt)
print(answer)  