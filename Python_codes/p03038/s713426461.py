n,m = map(int,input().split())
a = sorted(list(map(int,input().split())))
bc = sorted([list(map(int,input().split())) for _ in range(m)],key = lambda x:-x[1])
flag = 0
flag_2 = 0
#print(a,bc)
for i in range(n):
  if a[i] < bc[flag_2][1]:
    a[i] = bc[flag_2][1]
  else:
    break
  flag += 1
  if flag == bc[flag_2][0]:
    flag_2 += 1
    flag = 0
  if flag_2 == m:
    break
print(sum(a))