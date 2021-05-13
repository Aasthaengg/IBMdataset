M = int(input())
LL = input().split()
list1 =[]
for i in LL:
  a = int(i)
  list1.append(a)
list1.sort()
print(list1[-1] -list1[0])