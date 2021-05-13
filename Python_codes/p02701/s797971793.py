n = int(input())
products = []
for i in range(n):
    p = input()
    products.append(p)
print(len(set(products)))
