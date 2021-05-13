N = int(input())
L = [0]*N
L[0] = list(map(int, input().split()))
for i in range (1,N):
  L[i] = list(map(int, input().split()))
  L[i][0] += max(L[i-1][1], L[i-1][2])
  L[i][1] += max(L[i-1][0], L[i-1][2])
  L[i][2] += max(L[i-1][0], L[i-1][1])
print(max(L[N-1]))