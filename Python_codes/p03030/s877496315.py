N = int(input())
list1 = []
for i in range(N):
  aa = input().split()
  a = aa[0]
  b = -int(aa[1])
  xxx = [a,b,i]
  list1.append(xxx)
list1.sort()

for i in range(N):
  list1[i].append(i)

for i in range(N):
  for j in list1:
    if j[3] == i:
      print(j[2]+1)