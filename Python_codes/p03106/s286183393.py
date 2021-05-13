A, B, K = input().split(" ")
A, B, K = int(A), int(B), int(K)

res = []

for i in range(A, 0, -1):
  if A % i == 0 and B % i == 0:
    res.append(i)

print(res[K-1])