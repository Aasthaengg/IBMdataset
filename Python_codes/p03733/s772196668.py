N, T = map(int, input().split())
t = list(map(int,input().split()))
total = 0
i=0
while i<N-1:
  if t[i+1]-t[i]<T:
    total+=t[i+1]-t[i]
  else:
    total+=T
  i+=1
total+=T
print(total)