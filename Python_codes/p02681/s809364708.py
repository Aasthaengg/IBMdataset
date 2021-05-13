S = input()
T = input()
Alf = [chr(i) for i in range(ord('a'), ord('z')+1)]
for i in range(26):
  if T == S + Alf[i]:
    print("Yes")
    exit(0)
print("No")