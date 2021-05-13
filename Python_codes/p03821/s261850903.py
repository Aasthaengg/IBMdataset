n = int(input())
list_a = []
list_b = []
su = 0
for i in range(n):
  a,b = map(int,input().split())
  list_a.append(a)
  list_b.append(b)
list_a = list_a[::-1]
list_b = list_b[::-1]
for i in range(n):
  list_a[i] += su
  if list_a[i]%list_b[i]==0:
    continue
  else:
    x = list_b[i]-(list_a[i]%list_b[i])
    su += x
#  print(list_a)
print(su)
