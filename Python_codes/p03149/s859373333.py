N = list(map(int,input().split()))
list0_9 = [0 for i in range(10)]
for i in N:
  list0_9[i]+=1
if list0_9[1] == list0_9[4] == list0_9[7] == list0_9[9] == 1:
  print("YES")
else:
  print("NO")
