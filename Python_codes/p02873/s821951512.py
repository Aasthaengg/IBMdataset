import itertools as it

S = input()
R = [(k,len(list(g))) for k,g in it.groupby(S)]
#print(R)

tot = 0
n = 0
for k,val in R:
  if k == "<":
    n = val
    tot += n*(n+1)/2
  elif k == ">":
    tot += max(0,val-n)
    tot += val*(val-1)/2
    n = 0
  
print(int(tot))