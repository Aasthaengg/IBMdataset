s = input()
n = int(input())
a = ""
for i in range(0, len(s), n):
  a += s[i:i+1]
print(a)