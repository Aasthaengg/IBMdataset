import itertools
bells = list(map(int,input().split()))
ans = []
for a,b in itertools.combinations(bells,2):
  ans.append(a+b)
print(min(ans))