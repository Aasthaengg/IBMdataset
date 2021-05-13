S=input()

flag=False
for s in S:
  if flag==True and s=='F':
    print('Yes')
    exit()
  if flag==False and s=='C':
    flag=True
print('No')
