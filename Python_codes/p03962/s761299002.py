j = (input())

x = j.split()
y = []

for i in x:
  if(i not in y):
    y.append(i)
print(len(y))
