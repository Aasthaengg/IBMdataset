length = int(input())
string = input()
x = 0
m = 0
for i in string:
  if(i == "D"):
    x-=1
  if(i == "I"):
    x+=1
  if(m < x):
    m = x
print(m)