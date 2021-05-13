N = int(input())
S = input()

output = ""
for s in S:
  trans_s = chr((ord(s) - ord("A") + N) % 26 + ord("A"))
  output += trans_s

print(output)
