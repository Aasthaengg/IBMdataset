n = int(input())
a_list = []
for n_i in range(n):
  a = int(input())
  a_list.append(a)
print(len(set(a_list)))