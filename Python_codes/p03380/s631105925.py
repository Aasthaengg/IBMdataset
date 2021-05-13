import math
import itertools

def swap(a,b):
    return max(a,b),min(a,b)

def comb(n,r):
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

_ = input()
an = list(map(int,input().split()))
#an = [5,10,12]
an.sort()
target = an[-1]/2
res = min(enumerate(an), key=lambda x: abs(target - x[1]))
print(an[-1], res[1])

