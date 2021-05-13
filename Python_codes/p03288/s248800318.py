r = int(input())
a = "G"
if r < 1200:
  a = "B"
elif r < 2800:
  a = "R"
print("A{}C".format(a))