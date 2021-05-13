def fac_count( x, counter):
    i=2;
    while x > 1:
        if x%i == 0:
            counter[i] = counter.get(i,0) + 1
            x //= i
        else:
            i += 1
    return counter

n=int(input())
counter = {}
for i in range(2,n+1):
    counter = fac_count(i,counter)

fac = [0] * 5 #2,4,14,24,74回以上

for i in counter.values():
    if i>=2:  fac[0] += 1
    if i>=4:  fac[1] += 1
    if i>=14: fac[2] += 1
    if i>=24: fac[3] += 1
    if i>=74: fac[4] += 1

 #3*5*5 / 3*25 / 5*15 / 75
ans =   fac[1] * (fac[1]-1)//2 * (fac[0]-2) + fac[3] * (fac[0] - 1) + fac[2] * (fac[1] - 1) + fac[4]
print(ans)