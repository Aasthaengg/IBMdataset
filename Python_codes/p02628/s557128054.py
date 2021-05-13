n,k = map(int, input().split())

p_list=list(map(int, input().split()))

p_list.sort()

#print(p_list)
#money = p_list.sort()
pricelist = p_list[:k]
pricesum = 0
for i in pricelist:
  pricesum += i

print(pricesum)
