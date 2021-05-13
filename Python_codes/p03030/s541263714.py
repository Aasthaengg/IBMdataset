list = []
N = int(input())
for i in range(N):
  S, P = map(str, input().split())
  list.append((i+1, S, int(P)))
list = sorted(list, key=lambda x:(x[1], -x[2]))
 
for l in list:
  print(l[0])