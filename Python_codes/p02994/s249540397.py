N,L = map(int,input().split())
s = sum([L+i-1 for i in range(1,N+1)])
if L <= 0 and L+N-1 >= 0:
    print(s)
elif L > 0:
    print(s-L)
else:
    print(s-L-N+1)