n = int(input())
s = input()
if n % 2 == 1:
  print("No")
  exit()
for i in range(n//2):
  if s[i] == s[n//2+i]:
    continue
  else:
    print("No")
    exit()
print("Yes")