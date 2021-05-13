N = int(input())

product = []

for i in range(1,10):
    for j in range(1,10):
        product.append(i * j)

if N in product:
    result = 'Yes'
else:
    result = 'No'

print(result)
