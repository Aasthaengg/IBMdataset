#--A - Tenki

S = input()
T = input()
word = list(S)
result = list(T)

j = 0
for i in range(3):
  if (word[i] == result[i]):
    j = j + 1
  else:
    pass

print(j)
