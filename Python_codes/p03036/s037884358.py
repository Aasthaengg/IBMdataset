r, D, x2000=map(int, input().split())

def next(x):
    return r*x-D

year=[None]*11
year[0]=x2000
for i in range(0, 10):
    print(next(year[i]))
    year[i+1]=next(year[i])
