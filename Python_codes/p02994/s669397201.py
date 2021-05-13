n,l=map(int,input().split())
 
min_abs=99999999999
min_abs_i=-1
n_aji=0
for i in range(1,n+1):
  aji=l+i-1
  aji_abs=abs(aji)
  if aji_abs < min_abs:
    min_abs = aji_abs
    aji_abs_i = i
  n_aji+=aji
 
print(n_aji-(l+aji_abs_i-1))