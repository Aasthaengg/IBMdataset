N = int(input())
my_list = []
for i in range(1,N+1):
    l = list((input().split()))
    l.append(i)
    my_list.append(l)
 
my_list2 = sorted(my_list, key=lambda x:(x[0],-int(x[1])))
for i in my_list2:
  print(i[2])
 