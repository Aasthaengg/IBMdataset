W,N = map(int,input().split())
 
table = [10000000]*(W+1)
 
table[0] = 0
 
coin_list = list(map(int,input().split()))
 
for coin in coin_list:
    for i in range(coin,W+1):
        table[i] = min(table[i],table[i-coin]+1)
 
 
print("%d"%(table[W]))
