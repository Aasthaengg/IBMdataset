c = input()
l = [chr(i) for i in range(97, 97+26)]

for j in range(25):
  if l[j] == c:
    print(l[j+1])
    exit()