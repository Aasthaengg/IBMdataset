lst = input().split()

cor_lst = sorted(lst)

#print(cor_lst)

if int(cor_lst[0]) == int(cor_lst[1]) and int(cor_lst[0]) == int(cor_lst[2]):
  print("Yes")
else:
  print("No")