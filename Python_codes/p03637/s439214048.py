n = int(input())

a = list(map(int,input().strip().split()))

t_4 = 0
t_2 = 0
for i in a:
  if i%4==0:
    t_4+=1
  elif i%2==0:
    t_2+=1
other = len(a)-t_4-t_2
if other <= t_4:
  print("Yes")
elif other == t_4 +1:
  if t_2 > 0:
    print("No")
    exit()
  else:
    print("Yes")
    exit()
else:
  print("No")