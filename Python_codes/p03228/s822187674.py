a, b, k = map(int, input().split())

for i in range(k):
    if i % 2 == 0:
        if a % 2 == 1:
            a -= 1
        exchenge = a // 2
        a -= exchenge
        b += exchenge 
    if i % 2 == 1:
        if b % 2 == 1:
            b -= 1
        exchenge = b // 2
        b -= exchenge
        a += exchenge   
print(f'{a} {b}')