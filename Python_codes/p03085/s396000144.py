b = input()
s = "AGTC"
for i in range(4):
  if s[i] == b:
    print(s[(i+2)%4])