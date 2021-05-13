n = int(input())
a = sorted(list(map(int, input().split())),reverse=True)
d = {}
for i in a:
  try:d[i] += 1
  except:d[i] = 1

ans = 0
t = 0
for i in d:
  if(d[i] >= 4 and ans == 0):print(i*i);exit()
  if(d[i] >= 2 and ans == 2):print(t*i);exit()
  if(d[i] >= 2 and ans == 0):t=i;ans=2
print(0)