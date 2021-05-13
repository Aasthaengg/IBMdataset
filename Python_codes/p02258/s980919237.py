N = int(input())
list_price = [int(input()) for i in range(N)]
minv = list_price[0]
maxv = -10**9
for x in list_price[1:]:
    maxv = max(maxv, x - minv)
    minv = min(minv, x)        
print(maxv)