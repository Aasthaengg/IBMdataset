#辞書型リスト作成
dic ={
  "a":list(input()),
  "b":list(input()),
  "c":list(input())
}
#print(dic)

now = "a"
while True:
  if len(dic[now]) == 0:
    print(now.upper()) #大文字変換
    break
  now = dic[now].pop(0) #値削除