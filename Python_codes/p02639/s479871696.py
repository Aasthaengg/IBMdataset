str = input()
data = str.strip().split()
for i in range(5):
  if data[i] == "0":
     print(i+1)