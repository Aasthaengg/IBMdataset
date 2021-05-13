N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(M)]
R = sum(A,[])

for i in range(1,N+1):
    print(R.count(i))
