N = int(input())
li = list(map(int,input().split()))
li.sort(reverse = True)
al = 0
bob = 0
for i in range(N):
  if i % 2 == 0:
    al = al + li[i]
  else:
    bob = bob + li[i]
an = al - bob
print(an)