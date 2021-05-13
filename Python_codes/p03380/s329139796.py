n = int(input())
a = list(map(int,input().split()))
d = max(a)
f = d
for v in a:
  if abs(v-d/2) < abs(f-d/2):
    f = v
  elif abs(v-d/2) == abs(f-d/2):
    f = min(f,v)
print(d,f)