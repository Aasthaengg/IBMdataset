K,T=map(int,input().split())
a=list(map(int,input().split()))
A=max(a)
if A<0.5*K:
    print(0)
else:
    print(2*A-K-1)