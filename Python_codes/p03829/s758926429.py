m=lambda:map(int,input().split())
N,A,B=m();*X,=m()
print(sum(min(B,A*(X[i+1]-X[i]))for i in range(N-1)))