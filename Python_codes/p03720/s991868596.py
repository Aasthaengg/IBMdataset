[N, M] = list(map(int, input().split()))
list_cnt = []
for i in range(M):
  ab = list(map(int, input().split()))
  list_cnt.append(ab[0])
  list_cnt.append(ab[1])
for k in range(1, N+1):
  print(list_cnt.count(k))