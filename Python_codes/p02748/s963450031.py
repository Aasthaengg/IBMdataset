A, B, M = (int(x) for x in input().split())
al = [int(x) for x in input().split()]
bl = [int(x) for x in input().split()]
ml = [[int(x) for x in input().split()] for _ in range(M)]
"""
price = []
for l in ml:
    price.append(al[l[0]-1] + bl[l[1]-1] - l[2])
for x in al:
    for y in bl:
        price.append(x+y)
"""
price = [al[l[0]-1] + bl[l[1]-1] - l[2] for l in ml] + [min(al)+min(bl)] 
print(min(price))