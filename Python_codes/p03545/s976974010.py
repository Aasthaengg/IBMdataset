ABCD=input()
f=""
for bit in range(1<<3):
  f=ABCD[0]
  for i in range(3):
    if bit&(1<<i):
      f+="+"
    else:
      f+="-"
    f+=ABCD[i+1]
  if eval(f)==7:
    print(f+"=7")
    exit()
