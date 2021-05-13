s = input()
k = int(input())

ans = ""
for si in s:
  if si == "a":
    ans += "a"
    continue
  num = ord("z") - ord(si) + 1
  if num <= k:
    ans += "a"
    k -= num
  else:
    ans += si

if k > 0:
  num = k % 26
  if ord(ans[-1]) + num <= ord("z"):
    new_c = chr(ord(ans[-1]) + num)
  else:
    num -= ord("z") - ord(ans[-1])
    new_c = chr(ord("a") - 1 + num)
  print(ans[:-1] + new_c)
else:
  print(ans)


