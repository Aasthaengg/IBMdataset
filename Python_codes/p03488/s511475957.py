s = str(input())
x,y = map(int,input().split())
x_list,y_list = [],[]
l = s.split('T')

for i in range(0,len(l),2):
  x_list.append(len(l[i]))
for i in range(1,len(l),2):
  y_list.append(len(l[i]))

ans_x,ans_y = set(),set()

if s[0]=='F':
  ans_x.add(x_list[0])
  x_list=x_list[1:]
else:
  ans_x.add(0)
ans_y.add(0)

for i in x_list:
  ans = set()
  for j in ans_x:
    ans.add(i+j)
    ans.add(j-i)
  ans_x = ans
for i in y_list:
  ans = set()
  for j in ans_y:
    ans.add(i+j)
    ans.add(j-i)
  ans_y = ans
if x in ans_x and y in ans_y:
  print("Yes")
else:
  print("No")