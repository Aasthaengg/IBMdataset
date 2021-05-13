n=input()
for i in range(10):
  if n.count(str(i)*3):
    print('Yes')
    exit(0)
print('No')