n = int(input())
s = input()
ans = 0

for i in range(1000): #0~999を全探索
  flg1 = False #1桁目があるか
  flg2 = False #2桁目があるか
  flg3 = False #3桁目があるか
  one = str(i//100) #1桁目
  two = str(i%100//10) #2桁目
  three = str(i%10) #3桁目
  t = 0
  
  for j in range(n-2):
    if s[j] == one:
      flg1 = True
      t = j+1
      break
  for j in range(t,n-1):
    if s[j] == two:
      flg2 = True
      t = j+1
      break
  for j in range(t,n):
    if s[j] == three:
      flg3 = True
      t = j+1
      break
  if flg1 and flg2 and flg3:
    ans += 1
print(ans)