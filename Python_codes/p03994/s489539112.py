s = input()
k = int(input())
slen = len(s)
new_s = ""

for i in range(slen):
  val = (ord("z") + 1 - ord(s[i])) % 26
  if k >= val:
    k -= val
    new_s += "a"
  else:
    new_s += s[i]
    
if k > 0:
  tmp_val = ord(new_s[slen-1]) + k % 26
  if tmp_val > ord("z"):
    tmp_val -= 26
  new_s = new_s[:-1] + chr(tmp_val)

print(new_s)