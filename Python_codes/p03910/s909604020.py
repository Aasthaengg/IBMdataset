n = int(input())
ps = 0
for i in range(1,10**100):
    ps += i
    if ps >= n:
        ii = i
        break

for i in range(1,ii+1):
    if i == ps-n:
        continue
    else:
        print(i)
