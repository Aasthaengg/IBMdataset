import sys
from collections import Counter
read=sys.stdin.read

n,*a=map(int,read().split())
x=Counter(a)
print(sum(list(map(lambda n:n%2, list(x.values())))))