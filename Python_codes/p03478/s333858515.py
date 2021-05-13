N,A,B = map(int,input().split())
cnt = 0

for i in range(1,N+1):
  d_num = i
  s_sum = 0
  while d_num > 0:
    s_sum += (d_num % 10)
    d_num //= 10
  
  if A <= s_sum <=  B:
    cnt += i

print(cnt)
