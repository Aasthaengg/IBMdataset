import math

X = int(input())
absX = abs(X)
X = math.pow(X, 1/5)
#print(X)
X = math.floor(X)
#print(X)

Pow = []
Dif = []

for i in range(64):
    Pow.append(int(math.pow(i, 5)))


for i in range(1, 1000):
    Dif.append(i**5 - (i-1)**5)
    if ((i+1)**5 - i**5) > 1000000000:
        break
#print(len(Dif))

#print(Pow)
#print(Dif)

for n in range(len(Pow)):
    p = Pow[n]
    m = n
    while m < len(Pow):
        q = Pow[m]
        if p + q > absX:
            break
        #print('p: {}, q: {}'.format(p, q))
        if p + q == absX :
            #print(absX)
            if X < 0:
                print(-n, m)
            else:
                print(n, -m)
            exit(0)
        m += 1

for n in range(len(Dif)):
    sam = 0
    m = n
    while m < len(Dif):
        sam += Dif[m]
        if sam > absX:
            break
        #print('sam: {}'.format(sam))
        if sam == absX:
            if X <= 0:
                print(n, m+1)
            else:
                print(-n,-(m+1))
            exit(0)
        m += 1