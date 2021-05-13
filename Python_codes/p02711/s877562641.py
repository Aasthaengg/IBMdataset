n=str(input())
a=0
for i in range(len(n)):
    if int(n[i])==7:
        a=1
        break
if a==1:
  print('Yes')
else:
  print('No')