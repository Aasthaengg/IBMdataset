N = int(input())
A = list(map(int, input().split()))

if 0 in A:
    print(0)
    exit()
product = 1
for num in A:
    product = product * num
    if product > 10 ** 18:
        print(-1)
        exit()

print(product)