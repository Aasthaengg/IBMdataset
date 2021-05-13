N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


a_num, b_num, a_time, b_time = 0, 0, 0, 0

for n,b in enumerate(B):
  b_time += b
  b_num += 1
  if b_time > K:
    b_time -= b
    b_num -= 1
    break
    
ans = b_num

for n,a in enumerate(A):
  a_time += a
  a_num += 1
  time = a_time + b_time
  while time > K and b_num > 0:
    b_time -= B[b_num - 1]
    b_num -= 1
    time = a_time + b_time
  if time > K:
    break
  ans = max(ans, a_num + b_num)

print(ans)