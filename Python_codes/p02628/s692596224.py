n,k = map(int, input().split())
price_list = [int(x.strip()) for x in input().split()]
sorted_list = sorted(price_list)
ans = sum(sorted_list[:k])
print(ans)