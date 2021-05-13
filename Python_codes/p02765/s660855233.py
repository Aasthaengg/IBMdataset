N,R = map(int,input().split())
if N > 10:
  r = R
else:
  r = R + (100*(10-N))
print(r)
