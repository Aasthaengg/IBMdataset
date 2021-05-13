n, p = map(int,input().split())
num = list(map(int,input().split()))

semua_angka_genap = True
for i in num:
  if i % 2 == 1:
    semua_angka_genap = False

if semua_angka_genap:
  if p == 0:
    print(2**n)
  else:
    print(0)

else:
  print(2**(n-1))