N = int(input())
taka = list(map(int,input().split()))
exam = list(map(int,input().split()))

sa = list()
#　高橋くんがマイナスになっている部分を変更することでうまくいくかどうかを検索する
for t,e in zip(taka,exam):
  sa.append(t-e)
sa = sorted(sa)

minus = list(filter(lambda x:x<0,sa))
plus = list(filter(lambda x:x>0,sa))

sum_plus = 0
sum_minus = sum(minus)
if sum_minus == 0:
  print(0)
else:
  for idx,p in enumerate(plus[::-1]):
    sum_plus += p
    if sum_plus>=-sum_minus:
      print(idx+1+len(minus))
      break
  else:
    print(-1)
