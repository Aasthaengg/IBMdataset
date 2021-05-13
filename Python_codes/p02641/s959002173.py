X,N,*P = map(int,open(0).read().split())
if P != []:
  P = sorted(list(P),reverse=True)
else:
  print(X)
  exit()

min_diff = 101
min_val = 101

for i in range(101,-1,-1):
  #print(i,min_val,min_val)
  if not i in P:
    if abs(X-i) <= min_diff and min_val >=i:
      min_diff = abs(X-i)
      min_val = i
  ans = min_val
print(ans)