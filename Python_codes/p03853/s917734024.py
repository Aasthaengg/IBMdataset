H, W = map(int, input().split())
h = []* 2* H

for i in range(H):
  str_array = input()
  h.append(str_array)
  h.append(str_array)

for i in range(2* H):
  print(h[i])