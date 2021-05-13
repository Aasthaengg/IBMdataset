_, *a = map(int, open(0))
from collections import*
print(sum(map(lambda k:k%2, Counter(a).values())))