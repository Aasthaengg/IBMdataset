N,K = map(int,input().split())
A = [int(i) for i in input().split()]
S = sum(A)

def searchPrimeNum(N):
    max = int(N**0.5)
    seachList = [i for i in range(2,N+1)]
    primeNum = []
    while seachList[0] <= max:
        primeNum.append(seachList[0])
        tmp = seachList[0]
        seachList = [i for i in seachList if i % tmp != 0]
    primeNum.extend(seachList)
    return primeNum

plis = searchPrimeNum(40000)

lis = []
for p in plis:
    if S%p == 0:
        lis.append([p,1])
        S = S//p
        while S%p == 0:
            lis[-1][1] += 1
            S = S//p
    if S == 1:
        break
if S != 1:
    lis.append([S,1])

yakulis =[1]
for l in lis:
    for j in range(len(yakulis)):
        for k in range(l[1]):
            n = yakulis[j]
            yakulis.append(l[0]**(k+1)*n)
yakulis.sort(reverse=True)

s = True
for r in yakulis:
    B = [i%r for i in A]
    B.sort()
    le = -1
    ri = N
    while ri-le > 1:
        mid = (le+ri)//2
        pl = sum(B[:mid+1])
        mi = r*(N-1-mid) - sum(B[mid+1:])
        if pl > mi:
            ri = mid
        else:
            le = mid
    k = sum(B[:le+1])
    if k <= K:
        s = False
        print(r)
        break
if s:
    print(1)