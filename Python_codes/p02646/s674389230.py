a_now, a_speed = map(int, input().split(' '))
b_now, b_speed = map(int, input().split(' '))
t = int(input())

# print(a_now, a_speed, b_now, b_speed, t)

# speedの差分と現在の差分で割り切れればOK、割り切れなければダメ
if(a_speed < b_speed):
  caught = 'NO'
else:
  diff = abs(a_now - b_now)
  speed = a_speed - b_speed
  #print("現在の距離差は{0}. スピード差は{1}".format(diff, speed))
  if(diff == 0):
    caught = 'NO'
  elif(speed == 0):
    #print("speedが一緒なので終わらない")
    caught = 'NO'
  else:
    q = diff / speed
    #print("おいつくのは{0}秒後. 余りは{1}".format(q, mod))
    if(q <= t):
      caught = 'YES'
    else:
      caught = 'NO'

print(caught)