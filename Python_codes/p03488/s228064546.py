# -*- coding: utf-8 -*-
def check(z, zz, z_list):
  if len(z_list) == 0:
    if z != zz:
      return 0
    else:
      return 1
  else:
    z_n = len(z_list)
    z_hash = {}
    z_hash[0] = {}
    z_hash[0][zz] = 1
    z_hash[z_n] = {}
    z_hash[z_n][z] = 1
    for i in range(0,z_n):
      if i+1 not in z_hash:
        z_hash[i+1] = {}
        for b_z in z_hash[i]:
          a_z = b_z + z_list[i]
          z_hash[i+1][a_z] = 1
          a_z = b_z - z_list[i]
          z_hash[i+1][a_z] = 1
      else:
        for b_z in z_hash[i]:
          a_z = b_z + z_list[i]
          if a_z in z_hash[i+1]:
            return 1
          a_z = b_z - z_list[i]
          if a_z in z_hash[i+1]:
            return 1
        return 0
      if z_n-i-1 not in z_hash:
        z_hash[z_n-i-1] = {}
        for a_z in z_hash[z_n-i]:
          b_z = a_z + z_list[z_n-i-1]
          z_hash[z_n-i-1][b_z] = 1
          b_z = a_z - z_list[z_n-i-1]
          z_hash[z_n-i-1][b_z] = 1
      else:
        for a_z in z_hash[z_n-i]:
          b_z = a_z + z_list[z_n-i-1]
          if b_z in z_hash[z_n-i-1]:
            return 1
          b_z = a_z - z_list[z_n-i-1]
          if b_z in z_hash[z_n-i-1]:
            return 1
        return 0



s = input()
x, y = map(int, input().split())
data = s.split("T")
xx, yy = 0, 0
i = 0
x_list = []
y_list = []
for Fs in data:
  if len(Fs) == 0:
    i += 1
  else:
    if i == 0:
      xx = len(Fs)
    elif i % 2 == 0:
      x_list.append(len(Fs))
    else:
      y_list.append(len(Fs))
    i += 1
if check(x, xx, x_list) == 1 and check(y, yy, y_list) == 1:
  print("Yes")
else:
  print("No")