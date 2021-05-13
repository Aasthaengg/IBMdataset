
N,K = map(int,input().split())

A = list(map(int,input().split()))

lis = [0] * 41

for i in range(N):
    for j in range(41):
        if A[i] & (2**j) != 0:
            lis[j] += 1


now = 0
ans = 0
#print (lis)

for i in range(41):

    i = 40-i

    if lis[i] >= N / 2:
        ans += (2**i)*lis[i]

    else:
        if now + 2**i <= K:
            now += 2**i
            ans += (2**i) * (N - lis[i])
        else:
            ans += (2**i) * lis[i]

    #print (ans)

print (ans)
