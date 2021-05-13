A,B,C = (int(i) for i in input().split())

K = int(input())

ans = "No"

for i in range(K):
  if A < B*(2**i) and B*(2**i) < C*(2**(K-i)):
    ans = "Yes"
    break

print(ans)
