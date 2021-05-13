N,P=map(int,input().split())
o=len([i for i in input().split() if int(i)%2])
print(2**(N-1) if o else 2**N if P==0 else 0)
