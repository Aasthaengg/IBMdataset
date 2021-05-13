s = input()
t = [i for i in s]

for i in range(3):
  if t[i] == t[i+1]:
    ck = False
    break
else:
  ck = True

print('Good' if ck else 'Bad')