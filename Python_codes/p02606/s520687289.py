from math import ceil
l,r,d=map(int,input().split())
print(r//d-ceil(l/d)+1)
