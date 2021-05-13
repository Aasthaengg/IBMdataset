N=int(input())
for i in range(N,0,-1):
    if i**0.5%1==0:
        print(i)
        exit()