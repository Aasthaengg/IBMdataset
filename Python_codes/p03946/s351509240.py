n, t = map(int, input().split())
A = tuple(map(int, input().split()))
count = 0
maxdiff = 0
mina = 10**9+1
for a in A:
    mina = min(mina, a)
    diff = a - mina
    if diff > maxdiff:
        count = 1
        maxdiff = diff
    elif diff == maxdiff:
        count += 1
print(count)