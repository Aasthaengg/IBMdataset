n,a,b = map(int,input().split())

cnt = 0

n_min = (a * (n-1)) + b
n_max = (b * (n-1)) + a

if (n_max - n_min + 1) < 0:
    result = 0
else:
    result = n_max - n_min + 1
print(result)