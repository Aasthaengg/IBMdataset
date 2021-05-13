K,T = map(int,input().split())
A = list(map(int,input().split()))
a = max(A)
if a<=(K+1)//2:
    print(0)
else:
    print(2*a-K-1)