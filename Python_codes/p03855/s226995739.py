n, k, l = map(int, input().split(" "))

def find(list_path, x):
  if list_path[x] != x:
    list_path[x] = find(list_path, list_path[x])
  return list_path[x]

def union(list_path, x, y):
  x = find(list_path, x)
  y = find(list_path, y)
  if x != y:
    list_path[x] = min(x, y)
    list_path[y] = list_path[x]

list_road = [i for i in range(n)]
for _ in range(k):
  p, q = map(int, input().split(" "))
  union(list_road, (p - 1), (q - 1))
list_rail = [i for i in range(n)]
for _ in range(l):
  r, s = map(int, input().split(" "))
  union(list_rail, (r - 1), (s - 1))

dict_num_connect = {}
for i in range(n):
  dict_num_connect[list_road[i], list_rail[i]] = dict_num_connect.get(
      (find(list_road, i), find(list_rail, i)), 0) + 1

print(" ".join(str(dict_num_connect[list_road[i], list_rail[i]]) 
               for i in range(n)))  