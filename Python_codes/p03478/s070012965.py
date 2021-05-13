N,A,B = (int(X) for X in input().split())
Count = 0
for T in range(1,N+1):
    if A<=sum(int(X) for X in list(str(T)))<=B:
        Count += T
print(Count)