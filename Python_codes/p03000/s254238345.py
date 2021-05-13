NN = input().split()
N = int(NN[0])
X = int(NN[1])
LL = input().split()
list1 = [0]
for i in range(N):
  
  a = list1[i] + int(LL[i])
  list1.append(a)
count = 0
for i in list1:
  if int(i) <= X:
    count +=1
print(count)