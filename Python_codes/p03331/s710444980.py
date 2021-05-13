N = int(input())
mn=10**8
for A in range(1,N):
    B=N-A
    sm=0
    while A!=0:
        sm+=A%10
        A//=10
    while B!=0:
        sm+=B%10
        B//=10
    if mn>sm:
        mn=sm
print(mn)