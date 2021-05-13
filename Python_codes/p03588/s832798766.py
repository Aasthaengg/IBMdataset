n = int(input())
dat = []
for _ in range(n):
    a = tuple(map(int, input().split()))
    dat.append(a)
dat.sort(reverse=True)
print(dat[0][0] + dat[0][1])