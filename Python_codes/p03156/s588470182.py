n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
f = 0
s = 0
t = 0
for i in p:
  if i <= a:
    f += 1
  elif i <= b:
    s += 1
  else:
    t += 1
print(min(f,s,t))