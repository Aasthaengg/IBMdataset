s=input()
t=input()
s_lst = list(s)
t_lst = list(t)
count = 0
for a,b in zip(s_lst, t_lst):
  if a!=b: count +=1
print(count)