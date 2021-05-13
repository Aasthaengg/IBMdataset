N, M, K = map(int, input().split())
a_books = list(map(int, input().split()))
b_books = list(map(int, input().split()))
a_time = 0
b_time = 0
a_times = [0 for _ in range(N+1)]
b_times = [0 for _ in range(M+1)]
for i, a in enumerate(a_books):
  a_time += a
  a_times[i+1] = a_time
  
for i, b in enumerate(b_books):
  b_time += b
  b_times[i+1] = b_time
  
result = 0
l = 0
for i in range(N+1):
  if l == M:
    break
  while(l <= M):
    if a_times[N-i] + b_times[l] <= K:
      result = max(result, N-i+l)
      l += 1
    else:
      break
print(result)