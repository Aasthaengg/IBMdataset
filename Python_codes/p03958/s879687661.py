k,t = map(int,input().split())
A = list(map(int,input().split()))
M = max(A)
Os = sum(A)-M
if Os+1 >= M:
    print(0)
else:
    print(M-1-Os)