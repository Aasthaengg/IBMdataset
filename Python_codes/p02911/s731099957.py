n, k, q=map(int, input().split())
l = [k-q for _ in range(n)]
#print(l)
for i in range(q):
  l[int(input())-1]+=1
for s in l:
  if s>0:
    print("Yes")
  else:
    print("No")