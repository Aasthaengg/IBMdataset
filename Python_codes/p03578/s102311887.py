n = int(input())
dl = list(map(int,input().split()))
m = int(input())
tl = list(map(int,input().split()))
d_dic = dict()
t_dic = dict()
for d in dl:
  if d in d_dic:
    d_dic[d] += 1
  else:
    d_dic[d] = 1
for t in tl:
  if t in t_dic:
    t_dic[t] += 1
  else:
    t_dic[t] = 1
for v in t_dic.keys():
  if not v in d_dic.keys():
    print('NO')
    exit()
  if t_dic[v] > d_dic[v]:
    print('NO')
    exit()
print('YES')