fo=0
fou=[0]
se=0
sev=[0]
fl=False
while fo<100:
  fo+=4
  fou.append(fo)
while se<100:
  se+=7
  sev.append(se)
n=int(input())
for i in fou:
  for j in sev:
    if n==i+j:
      fl=True
      print("Yes")
      break
  if fl:
    break
else:
  print("No")
