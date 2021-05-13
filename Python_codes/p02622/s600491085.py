s=input()
list_s=list(s)
t=input()
count=0
list_t=list(t)
for i in range(0,len(list_s)):
  if(list_s[i] != list_t[i]):
    count+=1
  else:
    count+=0
    
print(count)