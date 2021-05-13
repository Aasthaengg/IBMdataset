n = int(input())
s = input()
ans = ""
for str in s:
  ords = ord(str)
  if ords + n > 90:
    ords -= 26
  ans += chr(ords + n)
print(ans)  