x=int(input())
hantei=1
for i in range(2,33):
  jou=2
  while i**jou<=x:
    if hantei< i**jou:
      hantei=i**jou
    jou+=1
print(hantei)