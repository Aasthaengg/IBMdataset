n, p = map(int,input().split())
num = list(map(int,input().split()))

semua_angka_genap = True
ada_angka_ganjil = False
for i in num:
  if i % 2 == 1:
    semua_angka_genap = False
    ada_angka_ganjil = True

if semua_angka_genap:
  if p == 0:
    print(2**n)
  else:
    print(0)

if ada_angka_ganjil:
  print(2**(n-1))

