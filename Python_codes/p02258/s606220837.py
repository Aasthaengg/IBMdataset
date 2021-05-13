n = int(input()) 
price = [int(input()) for i in range(n)]
maxp = price[1] - price[0]
minp = price[0]
for j in range(1, n):
    maxp = max([maxp, price[j] - minp])
    minp = min([minp, price[j]])
print(maxp)
