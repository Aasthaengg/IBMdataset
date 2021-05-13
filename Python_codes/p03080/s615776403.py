n = int(input())
s = input()

if len([i for i in s if i == "R"]) > len([i for i in s if i == "B"]):
  print("Yes")
  
else :
  print("No")