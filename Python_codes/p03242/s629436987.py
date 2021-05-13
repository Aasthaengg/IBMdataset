a = list(input())

for i in range(3):
  if a[i] == "9":
    a[i] = "1"
  else:
    a[i] = "9"
    
print(a[0]+a[1]+a[2])