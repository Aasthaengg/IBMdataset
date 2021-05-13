import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N,A,B = MI()
v = LI()
v.sort(reverse=True)

print(sum(v[0:A])/A)

kaijou = [1]
for i in range(1,N+1):
    kaijou.append(kaijou[-1]*i)

def nCr(n,r):
    if n < r:
        return 0
    else:
        return (kaijou[n]//kaijou[r])//kaijou[n-r]

if v[0] != v[A-1]:
    a,b = 0,0  # v[A-1] より大きい元の個数、v[A-1] と等しい元の個数
    for i in range(N):
        if v[i] > v[A-1]:
            a += 1
        elif v[i] == v[A-1]:
            b += 1
    print(nCr(b,A-a))
else:
    a = v.count(v[A-1])
    print(sum(nCr(a,i) for i in range(A,B+1)))
