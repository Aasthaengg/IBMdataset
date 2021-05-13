N,A,B=map(int,input().split())
max_=min(A,B)
min_=max(0,(min(A,B)-(N-max(A,B))))
print(max_,min_)
