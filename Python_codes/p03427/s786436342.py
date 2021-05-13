import itertools as it

N =  int(input())
n =list(map(str,range(10)))
ans = 0
for i in it.combinations_with_replacement(n,16):
  a = int("".join(i))
  if a <= N:
    b = sum(map(int,i))
    ans = max(ans,b)
print(ans)