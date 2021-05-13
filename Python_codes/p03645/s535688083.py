N, M = map(int, input().split())

dic = {1:set(), N:set()}

for _ in range(M):
  a,b = map(int, input().split())
  if a == 1:
    dic[1].add(b)
  elif b == N:
    dic[N].add(a)

for i in dic[1]:
  if i in dic[N]:
    print("POSSIBLE")
    exit()
    
print("IMPOSSIBLE")
