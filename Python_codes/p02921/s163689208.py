s=str(input())
y=str(input())
s=list(s)
y=list(y)
count=0
for i in range(0,3):
  if s[i]==y[i]:
    count=count+1
print(count)