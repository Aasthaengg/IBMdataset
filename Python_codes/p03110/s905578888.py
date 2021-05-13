otosidama=0.0
for i in range(int(input())):
  x, u = input().split()
  otosidama += float(x) if u=='JPY' else float(x)*380000.0
  
print(otosidama)