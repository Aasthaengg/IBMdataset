n =int(input())
s = input()
x,ans =0,0
for i in s:
  if i =="I":
    x +=1
    ans =max(x,ans)
  else:
    x-=1
    ans =max(x,ans)
print(ans)