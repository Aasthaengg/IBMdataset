MM = input().split()
A = int(MM[0])
B = int(MM[1])
K = int(MM[2])
list1 =[]
for i in range(1,101):
  if A%i ==0 and B%i ==0:
    list1.append(i)
print(list1[-K])
