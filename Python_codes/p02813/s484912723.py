N = int(input())
P = list(map(int, input().split()))    
Q = list(map(int, input().split()))

queue = [i for i in range(1, N+1)]
b = []

def pq(n,q):
    a = len(q) - 1
    if a == 0:
        n += q[0]
        return n
    else:
        plus = q.pop(0)
        return pq(n+plus*10**a, q)


def nBinarius(a, q):
    n = len(q) - 1
    if n == 0:
        b.append(a + q[0])
    else:
        j = 0
        for i in q:
            q.remove(i)
            nBinarius(a + i*(10**n), q)
            q.insert(j, i)
            j += 1
    return


p = pq(0, P)
q = pq(0, Q)
nBinarius(0, queue)
pn = 0
qn = 0
n = 0
for i in b:
    if p == i:
        pn = n
    if q == i:
        qn = n
    n += 1
        
print(abs(pn-qn))