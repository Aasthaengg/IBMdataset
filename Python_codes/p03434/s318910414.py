N = input()
MM = input().split()
list1 =[]
for i in MM:
  x = int(i)
  list1.append(x)
list1.sort(reverse = True)
total = 0
for i in range(len(list1)):
  if i%2 ==0:
    total += list1[i]
  else:
    total -= list1[i]
print(total)