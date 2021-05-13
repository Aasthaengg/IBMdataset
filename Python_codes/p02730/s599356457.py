string = input()
mid = len(string)//2

gnirts = string[::-1]
if(string != gnirts or string[:mid] != gnirts[mid+1:] or string[mid+1:] != gnirts[:mid]):
  print("No")
  exit()
print("Yes")