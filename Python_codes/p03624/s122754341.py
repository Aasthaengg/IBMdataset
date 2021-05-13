S = set(input())
Flag = [True]*26

for i in S:
  Flag[ord(i)-97] = False

for i in range(26):
  if Flag[i]:
    print(chr(97+i))
    exit()

print("None")