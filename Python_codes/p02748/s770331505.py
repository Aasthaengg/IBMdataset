A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
z = [list(map(int, input().split())) for i in range(M)]

price = min(a) + min(b)

for e in z:
    tmp_price = a[e[0]-1] + b[e[1]-1] - e[2]

    if(price > tmp_price):
        price = tmp_price

print(price)
