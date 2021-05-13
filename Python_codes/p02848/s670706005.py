N = int(input())
S = input()
R = ""
for i in range(len(S)):
  R += chr((ord(S[i]) - 65 + N) % 26 + 65)
print(R)