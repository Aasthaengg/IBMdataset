s=input()
a=[]
  
def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 
for i in range(len(s)):
  if i%2==0:
    a.append(s[i])
print(convert(a))