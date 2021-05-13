n = int(input())
dat = []
oddcnt = 0
for _ in range(n):
    x = int(input())
    dat.append(x)
    if x % 2 == 1:
        oddcnt += 1
if oddcnt == 0:
    print("second")
else:
    print("first")