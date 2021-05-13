import collections

n = int(input())
graph = collections.defaultdict(list)
for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

cur_f = [1]
cur_s = [n]
visit_f = {1}
visit_s = {n}
while cur_f or cur_s:
  temp_f = []
  for start in cur_f:
    for end in graph[start]:
      if end not in visit_f and end not in visit_s:
        temp_f.append(end)
        visit_f.add(end)
  cur_f = temp_f
  temp_s = []
  for start in cur_s:
    for end in graph[start]:
      if end not in visit_f and end not in visit_s:
        temp_s.append(end)
        visit_s.add(end)
  cur_s = temp_s

if len(visit_f) > len(visit_s):
  print("Fennec")
else:
  print("Snuke")