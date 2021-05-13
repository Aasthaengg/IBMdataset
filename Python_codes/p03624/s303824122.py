S=input()
set1=set(S)

for i in range(97,123):
  if chr(i) not in set1:
    print(chr(i))
    exit()
print('None')