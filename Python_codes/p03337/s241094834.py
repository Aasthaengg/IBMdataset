A, B = map(int, input().split())

AB_add = A + B
AB_dec = A - B
AB_mul = A * B

a = [AB_add, AB_dec, AB_mul]

a.sort()

print(a[2])
