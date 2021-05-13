N,K = map(int,input().split())
enemys = list(map(int,input().split()))
enemys = sorted(enemys,reverse = True)
if K >= N:
  print(0)
elif K == 0:
  print(sum(enemys))
else:  
  enemys = enemys[K:]
  print(sum(enemys))