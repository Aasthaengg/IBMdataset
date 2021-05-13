n = int(input())
s = input()
c = 0
for i in range(2,n):
  if s[i-2] == "A" and s[i-1] == "B" and s[i] == "C":
    c += 1
print(c)