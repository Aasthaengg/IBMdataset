def aaa(strArg):
  str = ''
  for c in strArg:
    str += ' ' + c
  return str

n = [int(input())]

house = ['0' * 30, '0' * 30, '0' * 30, '0' * 30]
hr = '#' * 20

for nn in range(n[0]):
  bfrv = [int(x) for x in input().split()]

  b = bfrv[0] - 1
  f = bfrv[1] - 1
  r = bfrv[2] - 1
  v = bfrv[3]

  pos = (f * 10) + r
  humal = int(house[b][pos]) + v

  house[b] = house[b][:pos] + str(humal) + house[b][pos + 1:]

for ii in range(4):
  print(aaa(house[ii][:10]))
  print(aaa(house[ii][10:20]))
  print(aaa(house[ii][20:]))
  if ii != 3:
    print(hr)