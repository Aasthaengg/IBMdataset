
def updiv(a,b):

    if a % b == 0:

        return a // b

    else:

        return a // b + 1


N,K = map(int,input().split())
ans = 0

if K == 0:
    print (N ** 2)

else:

    for i in range(N):

        i += 1

        if i < K:
            continue;

        ans += (i - K) * (N // i)

        nk = N - (N // i) * i

        ans += max(0 , nk - (K-1))

    print (ans)
