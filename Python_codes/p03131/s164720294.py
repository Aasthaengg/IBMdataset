K,A,B=map(int,input().split())
q,r=divmod(K-A+1,2)
print(max(A+q*(B-A)+r,K+1))