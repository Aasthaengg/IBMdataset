N,K = map(int,input().split())
if N ==1:
    ans=K
else:
    ans = K * ((K-1)**(N-1))

print(ans)