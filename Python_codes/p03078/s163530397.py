from collections import deque
X, Y, Z, K = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())), reverse=True)
C = sorted(list(map(int, input().split())), reverse=True)

A.append(-int(1e+100))
B.append(-int(1e+100))
C.append(-int(1e+100))

Aq = deque(A)
Bq = deque(B)
Ar = [Aq.popleft()]
Br = [Bq.popleft()]
maximum = min((len(A)-1) + (len(B)-1), 3001)
preA = Ar[0]
preB = Br[0]

while len(Ar) + len(Br) < maximum:
    if  Ar[0] - Aq[0] > Br[0] - Bq[0]:
        Br.append(Bq.popleft())
        preB = Br[-1]
    else:
        Ar.append(Aq.popleft())
        preA = Ar[-1]

AB = [Ar[i] + Br[j] for i in range(len(Ar)) for j in range(len(Br))]
AB = sorted(AB, reverse=True)

AB.append(-int(1e+15))

ABq = deque(AB)
Cq = deque(C)
ABr = [ABq.popleft()]
Cr = [Cq.popleft()]
maximum = min((len(AB)-1) + (len(C)-1), 3001)
preAB = ABr[0]
preC = Cr[0]
while len(ABr) + len(Cr) < maximum:
    if ABr[0] - ABq[0] > Cr[0] - Cq[0]:
        Cr.append(Cq.popleft())
        preC = Cr[-1]
    else:
        ABr.append(ABq.popleft())
        preAB = ABr[-1]

ABC = [ABr[i] + Cr[j] for i in range(len(ABr)) for j in range(len(Cr))]
ABC = sorted(ABC, reverse=True)

for i in range(K):
    print(ABC[i])
