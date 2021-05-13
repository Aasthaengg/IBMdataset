s=input()
numbers=[]
[numbers.append(int(s[i])) for i in range(4)]
for i in range(2**3):
  opes=[]
  count=numbers[0]
  for j in range(3):
    if (i>>j)&1:
      opes.append("+")
      count+=numbers[j+1]
    else:
      opes.append("-")
      count-=numbers[j+1]
  if count==7:
    print(numbers[0],end="")
    for k in range(3):
      print(opes[k],end="")
      print(numbers[k+1],end="")
    print("=",end="")
    print(count)
    exit()