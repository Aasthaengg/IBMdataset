from itertools import product
l= [int(input()) for _ in range(2)]
m=[int(input()) for _ in range(2)]
ans= min(x+y for x,y in product(l,m))
print(ans)