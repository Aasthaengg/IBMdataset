n,a,b,c,d=map(int, input().split())
s=list(input())

if d>c:
  #B→Aの順番でチェック
  for i in range(b-1,d-3):
    if "".join(s[i:i+2])=="##":
      print("No")
      exit()

  for i in range(a-1,c-3):
    if "".join(s[i:i+2])=="##":
      print("No")
      exit()
  #問題なければ終了
  print("Yes")

else:
  flag=False
  #BからDの間に3マス連続で空きがあるかチェック（AがBを抜かせるかどうか）
  for i in range(b-2, d-1):
    if "".join(s[i:i+3])=="...":
      flag=True
      break
  #抜かせる
  if flag:
    for i in range(a-1,c-3):
      if "".join(s[i:i+2])=="##":
        print("No")
        exit()
    print("Yes")
  #抜かせない
  else:
    print("No")