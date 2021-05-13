a=input()
ans=0
for i in a:
  ans = (ans+int(i))%9
print(["Yes","No"][ans>0])