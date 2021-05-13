N,T=map(int,input().split())
t=list(map(int,input().split()))
hiku=0
for i in range(N-1):
    if t[i]+T<t[i+1]:
        hiku+=t[i+1]-(t[i]+T)
print(t[-1]+T-hiku)