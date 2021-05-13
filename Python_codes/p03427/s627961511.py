N = list(map(int,list(input())))
if N[1:].count(9)==len(N)-1:
  ans = sum(N)
elif len(N)==1:
  ans = N[0]
else:
  ans = N[0]-1+9*(len(N)-1)
print(ans)