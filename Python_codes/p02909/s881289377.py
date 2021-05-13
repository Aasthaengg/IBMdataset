tod=input()
list=["Sunny", "Cloudy", "Rainy"]
count=0
for i in list:
  if count==2:
      print(list[0])
      break
  if list[count]==tod:
    print(list[count+1])
    break
  count+=1
