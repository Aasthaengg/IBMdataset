N = int(input())
S = input()
I = ord("A")
T = ""
for s in S:
  T += chr((ord(s)-I+N)%26+I)
print(T)