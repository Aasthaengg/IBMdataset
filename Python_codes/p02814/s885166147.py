import fractions
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

N,M = (int(x) for x in input().split())
a = list(map(int, input().split()))
temp = [a[0],a[0]//2]
broke = False
for i in range(1,N):
    gcd = xgcd(temp[0],a[i])
    if temp[1] % gcd[0] != (a[i]//2) % gcd[0]:
        broke = True
        break
    else:
        x = temp[1] + temp[0]*((a[i]//2)-temp[1])//gcd[0]*gcd[1]
        temp[0] = (temp[0] * a[i]) // fractions.gcd(temp[0], a[i])
        temp[1] = x % temp[0]
if broke:
    print('0')
else:
    dm = divmod(M,temp[0])
    if dm[1] >= temp[1]:
        print(dm[0]+1)
    else:
        print(dm[0])