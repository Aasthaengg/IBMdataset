# 座標A、速度V
a, v = map(int, input().split())

# 座標B、速度W
b, w = map(int, input().split())

# 時間T
t = int(input())

# 座標の差と速度の差
sa_x = abs(b-a)
sa_v = v-w

# 速度の差×時間が座標の差以上ならOK
if (sa_v * t >= sa_x):
  print('YES')
else:
  print('NO')