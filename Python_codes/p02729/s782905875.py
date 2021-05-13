def keisan(x):
  ret_val=0
  for i in range(1,x):
    ret_val+=i
  return ret_val

N,M=map(int,input().split())
print(keisan(N)+keisan(M))
