N, M, K = map(int,input().split())
jdg = 0
for L in range(1, N+1):
    for C in range(1, M+1):
        if ((M-C)*L + (N-L)*C == K or (M-C)*L + (N-L)*C == N*M-K) and jdg == 0:
            jdg += 1
            print("Yes")
            break
if jdg == 0 :
    print("No")