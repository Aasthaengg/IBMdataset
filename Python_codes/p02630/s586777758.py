n = int(input())
a = list(map(int,input().split()))
q = int(input())

dict_a = {}
current_sum = 0
for i in range(n):
  dict_a[a[i]] = dict_a.get(a[i],0)+1
  current_sum += a[i]

for i in range(q):
  b,c = map(int,input().split())
  diff = c-b
  
  rep_num = dict_a.get(b,0)
  current_sum += diff*rep_num
  print(current_sum)
  
  dict_a[b] = 0
  dict_a[c] = dict_a.get(c,0) + rep_num