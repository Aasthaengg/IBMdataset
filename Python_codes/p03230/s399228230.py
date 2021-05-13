import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
ans = []

N = I()

ansCandi = []
for i in range(1,1000):
    a = (i+1)*i/2
    ansCandi.append(a)

if N not in ansCandi:
    print("No")
else:
    a = ansCandi.index(N)+1
    A = [[0] * (a+1) for _ in range(a+1)]

#    print(a)
    k = int(1)
    for i in range(a+1):
        for j in range(i+1,a+1):
            A[i][j] = k
            A[j][i] = k
            k += 1

    print("Yes")
    print(a+1)

    for v in A:
        v.remove(0)
        v.insert(0,a)

    for v in A:
        print(*v)




