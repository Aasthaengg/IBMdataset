n = int(input())
a,b = map(int,input().split())
p = list(map(int,input().split()))
a1 = 0
a2 = 0
a3 = 0

for i in p:
  if i <= a:
    a1 += 1
  elif a+1 <= i and i <= b:
    a2 += 1
  else:
    a3 += 1

print(min(a1,a2,a3))