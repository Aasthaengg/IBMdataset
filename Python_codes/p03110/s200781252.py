N=int(input())
Y=0

for i in range(N):
    x, u=input().split()
    x=float(x)
    if u=="BTC":
        Y+=x*380000
    else:
        Y+=x

print(Y)