n = int(input())
l = [{} for d in range(n)]
for i in range(n):
  s,p = input().split()
  l[i] = {'City': s, 'Point': int(p), 'Number': i+1}
l.sort(key=lambda x: (x['City'],-x['Point']))
for num in l:
  print(num['Number'])