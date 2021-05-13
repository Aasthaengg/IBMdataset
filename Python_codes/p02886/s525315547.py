N = int(input())
D = list(map(int, input().split()))
su = 0

for j  in range(N-1):
  for k in range(j+1, N):
    su += D[j] * D[k]
print(su)