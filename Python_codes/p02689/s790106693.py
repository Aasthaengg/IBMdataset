import collections

n,m = list(map(int,input().split()))
n_list = list(map(int,input().split()))
eliminate_list = []

for i in range(0,m):
  a,b = list(map(int,input().split()))
  if n_list[a-1] > n_list[b-1]:
    eliminate_list.append(b-1)
  elif n_list[a-1] < n_list[b-1]:
    eliminate_list.append(a-1)
  else:
    eliminate_list.append(a-1)
    eliminate_list.append(b-1)

print(n - len(collections.Counter(eliminate_list)))