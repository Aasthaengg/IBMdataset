n=int(input())
tp=0
hp=0
for i in range(n):
  taro,hanako=(str(buff) for buff in input().split())
  if taro>hanako:
    tp+=3
  elif taro<hanako:
    hp+=3
  else:
    tp+=1
    hp+=1
print(tp,hp)

