n = int(input())
a_list = [int(input()) for _ in range(n)]

my_set = set()
for i in a_list:
  if i in my_set:
    my_set.remove(i)
  else:
    my_set.add(i)
print(len(my_set))