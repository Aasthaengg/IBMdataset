N_list = [int(e) for e in input().split()]

if N_list.count(1)==1 and N_list.count(9)==1 and N_list.count(7)==1 and N_list.count(4)==1:
  print("YES")
else:
  print("NO")