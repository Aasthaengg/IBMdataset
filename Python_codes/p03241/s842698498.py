n,m=map(int,input().split())

syou = m//n
amari = m%n

while True:
    if amari%syou == 0:
        print(syou)
        break
    else:
        amari+=n
        syou-=1
