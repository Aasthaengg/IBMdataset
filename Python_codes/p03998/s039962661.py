sa=list(input())
sb=list(input())
sc=list(input())
flg="a"

while True:
  if flg=="a":
    if len(sa)==0:
      break
    else:
      flg=sa[0]
      sa.pop(0)
  elif flg=="b":
    if len(sb)==0:
      break
    flg=sb[0]
    sb.pop(0)
  elif flg=="c":
    if len(sc)==0:
      break
    else:
      flg=sc[0]
      sc.pop(0)
print("A" if flg=="a" else "B" if flg=="b" else "C")