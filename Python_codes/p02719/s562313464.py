N,M = map(int,input().split())

ans = N

if N ==M or N%M ==0:
    print(0)

elif N < M:
    if abs(ans-M) > ans:
        print(ans)
    else:
        print(abs(ans-M))

else:
    print(min(N % M,abs((N % M) - M)))
