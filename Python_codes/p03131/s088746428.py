K,A,B=map(int,input().split())
k1=min(K,A-1)
k2=(K-k1)//2
k3=(K-k1)%2
print(1+k1+k3+k2*(max(A+2,B)-A))