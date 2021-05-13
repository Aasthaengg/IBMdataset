s = input()
l = [s[i] for i in range(len(s)) if i % 2 == 0]
for j in l:
  print(j,end="")