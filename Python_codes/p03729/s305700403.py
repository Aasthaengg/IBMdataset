lis = input().split()
lis_a = lis[0][len(lis[0])-1]
lis_bt = lis[1][0]
lis_bf = lis[1][len(lis[1])-1]
lis_c = lis[2][0]

if lis_a == lis_bt and lis_bf == lis_c:
  print("YES")
else:
  print("NO")