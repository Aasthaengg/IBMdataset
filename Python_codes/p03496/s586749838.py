n = int(input()) 
a = [int(item) for item in input().split()]

mina = min(a)
min_index = a.index(mina)
maxa = max(a)
max_index = a.index(maxa)

if abs(maxa) > abs(mina):
    sign = maxa
    sign_id = max_index
else:
    sign = mina
    sign_id = min_index

print(n + n-1)

if sign >= 0:
    for i in range(n):
        a[i] += sign
        print(sign_id+1, i+1)
    for i in range(n-1):
        a[i+1] += a[i]
        print(i+1, i+2)
else:
    for i in range(n):
        a[i] += sign
        print(sign_id+1, i+1)
    for i in range(n-1):
        a[n-i-2] += a[n-i-1]
        print(n-i, n-i-1)