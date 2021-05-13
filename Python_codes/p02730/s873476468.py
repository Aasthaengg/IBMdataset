s = input()
p ="Yes"
for i in range(len(s)//2):
  if s[i] != s[len(s) -1 -i]:
    p = "No"
for i in range(len(s)//2):
  if s[i] != s[len(s)//2 -1 -i]:
    p = "No"
print(p)