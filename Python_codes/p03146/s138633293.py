S = int(input())
a = S
list1=[a]
b = 1
while True:
  if a%2 ==0:
    a = a/2
    b +=1
    if a in list1:
      break
    list1.append(a)
  else:
    a = 3*a+1
    b+=1
    if a in list1:
      break
    list1.append(a)
print(b)