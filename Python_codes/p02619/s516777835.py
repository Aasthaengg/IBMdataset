import sys
d = int(sys.stdin.readline().rstrip())
list_c = list(map(int, sys.stdin.readline().rstrip().split()))
list_s = []
list_t = []
need = 0
for i in range(d):
  list_s.append(list(map(int, sys.stdin.readline().rstrip().split())))
for i in range(1, d+1):
  t = int(sys.stdin.readline().rstrip())
  list_t.append(t)
  need += list_s[i-1][t-1]
  MINUS = 0
  list_t1 = list_t[::-1]
  for j in range(1, 27):
    if not j in list_t1:
      MINUS += list_c[j-1] * len(list_t)
    else:
      MINUS += list_c[j-1] * list_t1.index(j)
  need -= MINUS
  print(need)