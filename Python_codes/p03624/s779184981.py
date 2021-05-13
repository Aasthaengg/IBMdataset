from string import ascii_lowercase
S=input()
ABC=[i for i in ascii_lowercase]
# print(ABC)

for i in ABC:
  if not i in S:
    print(i)
    break
else:
  print('None')