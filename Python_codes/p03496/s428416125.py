N = int(input())
A = list(map(int, input().split()))
INF = 10**6+1
MIN, MAX = INF, -INF
for i, a in enumerate(A, start=1):
    if a < MIN:
        MIN, MINi = a, i
    if MAX < a:
        MAX, MAXi = a, i
if MAX < 0 or (MAX + MIN < 0):
    print(2*N-1)
    for i in range(1, N+1):
        print(MINi, i)
    for i in range(2, N+1)[::-1]:
        print(i, i-1)
    quit()
flag = 0
if MIN < 0 and MAX + MIN >= 0:
    print(2*N-1)
    flag = 1
    for i in range(N):
        print(MAXi, i+1)
if not flag:
    print(N-1)
for i in range(1, N):
    print(i, i+1)
