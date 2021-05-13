H1, M1, H2, M2, K = map(int, input().split())

if(M2 < M1):
    m = 60-(M1-M2)
    print((H2-H1-1)*60+m-K)
else:
    print((H2-H1)*60+(M2-M1)-K)