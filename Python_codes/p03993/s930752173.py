N=int(input())
a = [int(i) for i in input().split() ]

nk = [0]*N
count = 0
for k,v in enumerate(a):
  if k+1 != v :
    nk[k] = v
    if nk[v-1] == k+1 :
      count += 1

print(count)
