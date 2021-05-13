n = int(input())
dat = list(map(int, input().split()))
dat.sort()
total = 0
ind = 0
for i in range(n-1):
    total += dat[i]
    if total * 2 < dat[i+1]:
        ind = i+1
print(n-ind)
