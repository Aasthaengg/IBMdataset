N = int(input())

A = map(int, input().split())
ABI = sorted(((a, max(N-i, i-1)*a, i) for i, a in enumerate(A, 1)), reverse=True)

prev = [0]
for k, (a, b, i) in enumerate(ABI):
  curr = [0]*(k+2)
  for l in range(k+1):
    curr[l] = max(curr[l], prev[l]+abs(N-i-k+l)*a)
    curr[l+1] = prev[l]+abs(i-l-1)*a

  prev = curr

print(max(prev))
