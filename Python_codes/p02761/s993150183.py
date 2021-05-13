N,M = map(int,input().split())
S = [list(map(int,input().split())) for _ in range(M)]
if N != 1:
    for i in range(M):
        if S[i][0] == 1 and S[i][1] == 0:
            print(-1)
            exit()
h,t,o = 0,0,0
if N != 1:
    h = 1
b_h,b_o,b_t = 0,0,0
for i in range(M):
    if S[i][0] == 3:
        if b_o == 1:
            if S[i][1] != o:
                print(-1)
                exit()
        o = S[i][1]
        b_o = 1
    elif S[i][0] == 2:
        if b_t == 1:
            if S[i][1] != t:
                print(-1)
                exit()
        t = S[i][1]
        b_t = 1
    else:
        if b_h == 1:
            if S[i][1] != h:
                print(-1)
                exit()
        h = S[i][1]
        b_h = 1
if N == 3:
    print(100*h+10*t+o)
elif N == 2:
    print(10*h+t)
else:
    print(h)