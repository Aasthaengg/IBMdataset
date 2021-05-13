n, m = map(int, input().split())
minmax = [n, m]
result = abs(n-m)
limit = 10**9+7

def lp(animal):
    row = 1
    for i in range(2, animal+1):
        row = row % limit * i 
    return row

if result >= 2:
    print(0)
    exit()

row = lp(min(minmax))
if n == m:
    print(row * row * 2 % limit)
else:
    print(row * row * max(minmax) % limit)

