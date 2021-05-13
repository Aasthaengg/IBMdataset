A,B,K=map(int,input().split())
S=set()
for i in range(1,min(A+1,B+1)):
    if A%i==0 and B%i==0:
        S.add(i)
print(sorted(S)[::-1][K-1])