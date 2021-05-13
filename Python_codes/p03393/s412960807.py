s = list(input())
n = len(s)

if n!=26:
  for i in [chr(ord('a') + i) for i in range(26)]:
    if not i in s:
      tmp=i
      break
  s.append(tmp)
  print("".join(s))

else:
  if "".join(s)=="zyxwvutsrqponmlkjihgfedcba":
    print(-1)

  else:
    for j in range(n)[::-1]:
      for k in range(1,122-ord(s[j])+1):
        tmp = chr(ord(s[j])+k)
        if tmp not in s[:j]:
          s[j]=tmp
          del s[j+1:]
          print("".join(s))
          exit()