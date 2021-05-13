n = int(input())
sl = list(input())
s2 = input()

c = []
before = sl[0]
for s in sl[1:]:
   if before == s:
      c.append(1)
      before = ""
   elif before != s and before != "":
      c.append(0)
      before = s
   else:
      before = s
if before != "":
   c.append(0)

if c[0] == 1:
   ans = 6
else:
   ans = 3
for i in range(len(c)-1):
   if c[i] == 1 and c[i+1] == 0:
      pass
   elif c[i] == 1 and c[i+1] == 1:
      ans *= 3
      ans %= 1000000007
   else:
      ans *= 2
      ans %= 10**9 + 7

print(ans)
