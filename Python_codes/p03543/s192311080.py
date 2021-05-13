n=input()
ans="No"
for i in range(2):
 if n[i]==n[i+1]==n[i+2]:
   ans="Yes"
print(ans)