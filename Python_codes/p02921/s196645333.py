pred = input()
real = input()
tmp=0
for i in range(3):
  if pred[i] == real[i]:
    tmp += 1
print(tmp)