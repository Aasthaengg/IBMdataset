n = int(input())
tree = [[] for i in range(n)]
d_list = [0]*n

stack = []
for i in range(n-1):
  u,v,w = map(int,input().split())
  tree[u-1].append((u-1,v-1,w))
  tree[v-1].append((v-1,u-1,w))
while len(tree[0]) > 0:
  e = tree[0].pop()
  stack.append(e)
#print(stack)
while len(stack) > 0:
  u,v, w = stack.pop()
  if d_list[v] == 0:
    d_list[v] = d_list[u]+w
  while len(tree[v]) > 0:
    e = tree[v].pop()
    stack.append(e)
  #print(stack)
for v in d_list:
  if v % 2 == 0:
    print(0)
  else:
    print(1)
