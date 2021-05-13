N,K,S = map(int, input().split())
c = 0
for i in range(N):
    if c < K :
        print(S, end = ' ')
        c += 1
    else:
        if S < 10** 9:
            print(S+1, end = ' ')
        else:
            print(1, end=' ')
