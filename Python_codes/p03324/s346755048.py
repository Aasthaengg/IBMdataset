D,N = map(int,input().split())
base = pow(100,D)
cnt = 0
now = 0
while cnt < N:
  now += base
  if now%(base*100) != 0:
    cnt += 1
  if cnt == N:
    print(now);exit()