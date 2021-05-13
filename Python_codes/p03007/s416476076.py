from heapq import heappop,heappush
n = int(input())
A = sorted(list(map(int,input().split())))
P = []
M = []
if n == 2:
    print(A[1]-A[0])
    print(A[1],A[0])
    exit()
def move():
    while len(P)!= 1:
        mm = heappop(M)
        pp = heappop(P)
        print(mm,pp)
        heappush(M,mm-pp)
    while len(M) != 0:
        mm = heappop(M)
        pp = heappop(P)
        print(pp,mm)
        heappush(P,pp-mm)
for a in A:
    if a>=0:
        P.append(a)
    else:
        M.append(a)

if A[-1]>=0 and A[0]<0:
    print(sum(abs(a) for a in A))
elif A[0]>=0:
    print(sum(A)-min(A)*2)
    mm = heappop(P)
    pp = heappop(P)
    print(mm,pp)
    heappush(M,mm-pp)
else:
    print(sum(abs(a) for a in A)+max(A)*2)
    mm = M[-1]
    pp = M[-2]
    print(mm,pp)
    M = M[:-2]
    heappush(P,mm-pp)
move()