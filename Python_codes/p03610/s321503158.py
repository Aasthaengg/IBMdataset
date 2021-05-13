s= input()
ans= ""
for i in range(int((len(s)+ 1)/ 2)):
  ans+= s[i* 2]
  
print(ans)