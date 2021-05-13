n = int(input())
a = list(map(int,input().split()))
a_dic = dict()
a_set = set()
for num in a:
  if num in a_dic:
    a_dic[num] += 1
  else:
    a_dic[num] = 1
  a_set.add(num)
k = len(a_dic)
a_set = list(a_set)
if k == 1:
  if 0 in a_dic:
    if a_dic[0] == n:
      print('Yes')
      exit()
elif k == 2:
  if a_dic[0] == n/3 and a_dic[a_set[1]] == 2*n/3:
    print('Yes')
    exit()
elif k == 3:
  if a_set[0] ^ a_set[1] ^ a_set[2] == 0:
    if a_dic[a_set[0]] == a_dic[a_set[1]] == a_dic[a_set[2]] == n/3:
      print('Yes')
      exit()
print('No')