N,M,K = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sum_time = 0
now_read_book = 0
ans = 0
now_A = -1

for i in range(N):
  if sum_time + A[i] <= K:
    sum_time += A[i]
    now_read_book += 1
    now_A = i
  else:
    break
ans = now_read_book

for i in range(M):
  if sum_time + B[i] > K:
    while sum_time + B[i] > K and now_A >= 0:
      sum_time -= A[now_A]
      now_A -= 1
      now_read_book -= 1
  if sum_time + B[i] <= K:
    sum_time += B[i]
    now_read_book += 1
  else:
    break
  if now_read_book > ans:
    ans = now_read_book
print(ans) 
