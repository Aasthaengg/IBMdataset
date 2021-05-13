count=0
while True:
  inputnumber = int(input())
  if inputnumber == 0:
    break
  else:
    print("Case",count+1,end="")
    print(":",inputnumber)
    count+=1