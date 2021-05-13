targ = ord("A")
n = int(input())
s = input()
ansl = []
for i in s:
  ansl.append(chr((ord(i)-targ+n)%26 + targ))
print("".join(ansl))