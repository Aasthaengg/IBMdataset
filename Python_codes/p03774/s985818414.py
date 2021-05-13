N, M = map(int, input().split())
# ab = [int(x) for _ in range(N) for x in input().split()]
ab = [list(map(int, input().split())) for _ in range(N)]
cd = [list(map(int, input().split())) for _ in range(M)]

for st in range(len(ab)):
    dis = [abs(ab[st][0] - cd[cp][0]) + abs(ab[st][1] - cd[cp][1])  for cp in range(len(cd))]
    print(dis.index(min(dis))+1)