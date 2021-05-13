N, M = map(int,input().split())
brd = [list(map(int, input().split())) for i in range(M)]
nbrd = sum(brd, [])
for i in range(1, N+1):
    print(nbrd.count(i))