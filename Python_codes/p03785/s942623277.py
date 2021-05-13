n , c , k = map(int,input().split()) # n人数、cバスに乗れる数、k怒り出す時間
t = [int(input()) for _ in range(n)]

#n,c,k = 6,3,3
#t = [7,6,2,8,10,6]

t = sorted(t)

jyokyaku = 0
bus = 0
for i in t:

  if jyokyaku == 0: #バス最初の乗客
    bus += 1
    angrytime = i + k
    jyokyaku += 1
    if jyokyaku == c: #定員になりバス出発
      jyokyaku = 0

  else: 
    if i <= angrytime: #最初の乗客がキレる前だったら乗れる
      jyokyaku += 1
      if jyokyaku == c: #定員になりバス出発
        jyokyaku = 0

    else: #もうバス出発してたので最初の乗客になった
      bus += 1
      jyokyaku = 1
      angrytime = i + k

print(bus)


