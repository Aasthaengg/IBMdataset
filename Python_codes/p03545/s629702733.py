s=list(input())
d=["+","-"]
for i in d:
  for j in d:
    for k in d:
      if eval(s[0]+i+s[1]+j+s[2]+k+s[3])==7:
        ans=s[0]+i+s[1]+j+s[2]+k+s[3]
        
print(ans+"=7")