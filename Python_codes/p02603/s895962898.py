n=int(input())
#n,k=map(int,input().split())
al=list(map(int,input().split()))
#l=[list(map(int,input().split())) for i in range(n)]
stock = 0
money = 1000
for i in range(n-1):
    sell = stock*al[i]
    stock = 0
    money += sell
    if al[i] < al[i+1]:# buy
        buynum = money//al[i]
        stock= buynum
        money -= buynum*al[i]

print(money + stock*al[n-1])
