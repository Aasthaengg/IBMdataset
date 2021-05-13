op = input()
count = 0
for i in op:
  if(i == "-"):
    count-=1
  elif(i == "+"):
    count +=1
print(count)