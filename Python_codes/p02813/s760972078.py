import itertools
N=int(input())
ListP = tuple(map(int, input().split()))
ListQ = tuple(map(int, input().split()))
s_l = set(ListP)
Per = list(itertools.permutations(s_l))
Per.sort()
mid1 = 0
mid2 = 0
for i in range(len(Per)):
  if Per[i] == ListP:
    mid1 = i+1
  if Per[i] == ListQ:
    mid2 = i+1
res = abs(mid1 -mid2)
print(res)