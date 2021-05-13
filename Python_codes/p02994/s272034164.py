N,L = map(int,input().split())
R = L+N-1
if L <= 0 <= R:
    print(sum(range(L,R+1)))
elif L > 0:
    print(sum(range(L+1,R+1)))
else:
    print(sum(range(L,R)))
