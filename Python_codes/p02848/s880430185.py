n = int(input())
s = input()
ans = ""
for i in s:
  t = ord(i)+n
  if t <= 90:
    ans += chr(t)
  elif t > 90:
    ans += chr(ord("A")+(abs(90-t))-1)
print(ans)