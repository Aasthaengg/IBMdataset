N = int(input())
NN = input().split()
D = int(NN[0])
X = int(NN[1])
count = 0
list1 =[]
for i in range(N):
  a = int(input())
  list1.append(a)
for i in list1:
  x = 1
  while x <= D:
    count +=1
    x += i
print(count+X)