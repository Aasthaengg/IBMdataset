N, K = map(int,input().split())
A = list(map(int,input().split()))


if (N-K)%(K-1)==0:
    ans = 1+(N-K)//(K-1)
else:
    ans = 2+(N-K)//(K-1)

print(ans)
