S = input()

Alpha = "abcdefghijklmnopqrstuvwxyz"
for i in Alpha:
  if i not in S:
    print(i)
    exit()
print("None")