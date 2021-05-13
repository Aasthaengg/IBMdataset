n = int(input())
result = ""

while n>0:
  if n%26 == 0:
    result = "z" + result
    n=n//26-1
  else:
    result= (chr(ord("a")+n%26-1)) + result
    n=n//26
  
print(result)