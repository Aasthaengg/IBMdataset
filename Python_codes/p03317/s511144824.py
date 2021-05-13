[N,K] = list(map(int,input().split()))
A = list(map(int,input().split()))

if (N-1)%(K-1)==0:
    out=(N-1)//(K-1)
else:
    out=(N-1)//(K-1)+1

print(out)
