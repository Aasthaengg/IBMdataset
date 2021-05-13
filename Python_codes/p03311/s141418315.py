n = int(input())
a = list(map(int, input().split()))
inf = 10**16

def func(b):
    return sum([abs(a[i]-(b+i+1)) for i in range(n)])

# 3分探索を行う
low = -inf
high = inf

while abs(high-low) > 0.01:
    c1 = (low*2 + high)/3
    c2 = (low + high*2)/3

    if func(c1) > func(c2):
        low = c1
    else:
        high = c2
mid = (high+low)/2
ans = min(func(int(mid)), func(int(mid+1)), func(int(mid-1)))
print(ans)
