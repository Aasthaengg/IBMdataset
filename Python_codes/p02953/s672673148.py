N=int(input())
H=list(map(int,input().split()))
H.reverse()
for i in range(N-1):
  diff=H[i+1]-H[i]
  if diff==1:
    H[i+1]-=1
  elif diff>1:
    print('No')
    exit()
  else:
    pass
print('Yes')
