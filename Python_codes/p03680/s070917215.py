N = int(input())
list1 = []
for i in range(N):
  a = int(input())
  list1.append(a-1)

count =0
x = 0
while x != 1 and count < 100000:
  count +=1
  x = list1[x]
  
if count < 100000:
  print(count)
else:
  print(-1)
