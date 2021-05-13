#連想配列（Ｄｉｃｔを使った配列操作）
N = int(input())
li = []
dict1 = {}
for _ in range(N):
  li.append(int(input()))



for i in range(N):
  if str(li[i]) in dict1:
    #print("delete",li[i])
    del dict1[str(li[i])]
  else:
    #print("add",li[i])
    dict1[str(li[i])] = '0'

print(len(dict1))