n = int(input())
dat = list(map(int, input().split()))
s = sum(dat) / n
mind = -1
mval = 9999
for i in range(n):
    if abs(dat[i] - s) < mval:
        mval = abs(dat[i] - s)
        mind = i
print(mind)