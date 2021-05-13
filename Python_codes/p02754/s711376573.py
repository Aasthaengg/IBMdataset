N,A,B = map(int,input().split())

N_syo = N//(A+B)
N_amari = N%(A+B)
ans = 0

if B == 0:
    print(N)

elif N_amari == 0:
    print(N_syo*A)
else:
    ans += N_syo*A
    N -= N_syo*(A+B)
    if N <= A:
        ans += N
        print(ans)
    else:
        ans += A
        print(ans)
