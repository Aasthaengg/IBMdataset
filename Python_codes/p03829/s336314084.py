N,A,B = map(int, input().strip().split(' '))
X = list(map(int, input().strip().split(' ')))

ans = 0
for i in range(N-1):
  ans += min(A*(X[i+1]-X[i]), B)
print(ans)