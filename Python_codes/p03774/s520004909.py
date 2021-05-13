N,M = map(int,input().split())

AB = [list(map(int,input().split())) for _ in range(N)]

CD = [list(map(int,input().split())) for _ in range(M)]

for a,b in AB:
    tmp_point = -1
    tmp_root = 100000000000
    for i,cd in enumerate(CD):
        c,d = cd
        if abs(a-c)+abs(b-d) < tmp_root:
            tmp_root = abs(a-c)+abs(b-d)
            tmp_point = i+1
    print(tmp_point)