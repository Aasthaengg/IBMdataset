from functools import reduce
from operator import mul
from itertools import product
N,*A=map(int, open(0).read().split())
print(sum(reduce(mul, prod)%2==0 for prod in product(*[(a-1,a,a+1) for a in A])))