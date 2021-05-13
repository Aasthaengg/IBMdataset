n=int(input())
a=[0]+sorted(list(map(int,input().split())))
x=a[-1]
m=a[-1]
for i in a:
  if m>abs(i-x/2):
    y=i
    m=abs(i-x/2)
print(x,y)