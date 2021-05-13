N = int(input())
S = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ""

for i in S:
  for j in range(len(alphabet)):
    if i == alphabet[j]:
      res += alphabet[j + N]
      break
print(res)