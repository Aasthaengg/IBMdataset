n = int(input())
dat = list(map(int, input().split()))
maxval = -9999999999999999999
maxind = -1
numminus = 0
dat2 = []

for i in range(n):
    if dat[i] < 0:
        numminus += 1
    dat2.append(abs(dat[i]))

dat2.sort()
#print(numminus)
#print(dat2)

if numminus %2 == 0:
    print(sum(dat2))
else:
    dat2[0] *= -1
    print(sum(dat2))

