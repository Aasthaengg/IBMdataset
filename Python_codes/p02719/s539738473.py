a,b=map(int,input().split())
n = a // b
res = a - n*b
res = min(abs(res-b),res)
print(res)