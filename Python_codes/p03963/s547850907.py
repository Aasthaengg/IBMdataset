N,K=input().split()
N=int(N)
K=int(K)

#1個目・・・K通り
#2個目～・・・K-1通り
ans=K*((K-1)**(N-1))
print(ans)