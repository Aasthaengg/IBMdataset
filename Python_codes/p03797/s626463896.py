N,M = list(map(int,input().strip().split()))

if 2*N > M:
  res = M // 2
else:
  res =  (M - 2*N)//4 + N

print(res)