N,A,B,*P=map(int, open(0).read().split())
S=[0]*3
f=lambda p:(A+1<=p)+(B+1<=p)
for p in P:
    S[f(p)]+=1
print(min(S))