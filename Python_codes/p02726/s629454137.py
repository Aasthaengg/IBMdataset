
N, X, Y = map(int, input().split())
X -= 1; Y -= 1

pat = [0]*(N-1)

for i in range(N):
  for j in range(i+1, N):
    d = min(abs(i-j), abs(X-i)+1+abs(j-Y))
    pat[d-1] += 1

for i in range(N-1):
  print(pat[i])