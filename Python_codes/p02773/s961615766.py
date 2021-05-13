N = int(input())
hashmap = {}
Array = [[] for _ in range(N+1)]
for _ in range(N):
  st = input()
  if st not in hashmap:
    hashmap[st] = 0
  hashmap[st]+=1
max_num = max(hashmap.values())
tup = []
for k,v in hashmap.items():
  if v == max_num:
    tup.append(k)
tup.sort()
for i in tup:
  print(i)