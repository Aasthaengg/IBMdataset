import math
import copy

n,k = map(int,input().split())
neko = k * (k-1)**(n-1)
print(neko)