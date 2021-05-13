# C 白昼夢

s = input()[::-1]

cnt = 0
while cnt < len(s):
  if not s[cnt:cnt+7] == "remaerd":
    if not s[cnt:cnt+6] == "resare":
      if not s[cnt:cnt+5] in ["maerd", "esare"]:
        print("NO")
        exit()
      else:
        cnt += 5
    else:
      cnt += 6
  else:
    cnt += 7
print("YES")