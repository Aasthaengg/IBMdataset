#-------------
N = int(input())
#-------------

C_list=[]

for i in range(26):
  for j in range(15):
    C_list.append(4*i + 7*j)

cnt = 0
for i in range(len(C_list)):
  if C_list[i] == N:
    cnt += 1

if cnt >= 1:
  print("Yes")
else:
  print("No")