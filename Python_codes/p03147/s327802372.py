n = int(input())
dat = list(map(int, input().split()))
res = 0
for j in range(n):
    for i in range(1, 101):
        if dat[j] >= i and (j == 0 or dat[j-1] < i):
            res += 1
print(res)
