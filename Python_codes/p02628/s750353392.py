k, n = map(int,input().split())
price = list(map(int,input().split()))
price.sort()

print(sum(price[0:n]))