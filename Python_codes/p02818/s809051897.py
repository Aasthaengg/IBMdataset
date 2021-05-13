A,B,K=map(int,input().split())
if A >= K:print(str(A-K)+' '+str(B))
if A < K and A+B>=K:print(str(0)+' '+str(A+B-K))
if A < K and A+B<K:print('0 0')