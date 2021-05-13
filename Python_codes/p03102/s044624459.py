N,M,C = map(int,input().split())
B = list(map(int,input().split()))

cnt = 0
for _ in range(N):
  A = list(map(int,input().split()))
  val = sum([a*b for a,b in zip(A,B)])
  if val > -C:
    cnt += 1
    
print(cnt)