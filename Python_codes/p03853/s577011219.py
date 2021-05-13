H, W = input().strip().split()
H, W = [int(H), int(W)]

data_list = []
#data_list = [ list(map(str,input().split(" "))) for i in range(H)]
for i in range(H):
  l = input()
  data_list.append(l)
  data_list.append(l)
  
for i in data_list:
  print(i)