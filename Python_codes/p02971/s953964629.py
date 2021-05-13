n=int(input())
l=[int(input()) for i in range(n)]

max_num=max(l)
max_index=l.index(max(l))

for i in range(n):
  if i!=max_index:
    print(max_num)
  else:
    l.remove(max_num)
    print(max(l))