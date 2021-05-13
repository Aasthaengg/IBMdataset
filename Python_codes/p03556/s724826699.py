N=int(input())
while N:
    if N**0.5%1==0:
        print(N)
        break
    else:
        N-=1