ans = "CODEFESTIVAL2016"
inp = input()

num = 0
for a,c in zip(ans, inp):
  if a != c:
    num += 1

print(num)