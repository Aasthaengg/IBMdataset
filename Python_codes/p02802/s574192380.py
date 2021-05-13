N, M = map(int,input().split())
results = [0 for _ in range(N+1)]
wa_list = [0 for __ in range(N+1)]
ac_cnt = 0
wa_cnt = 0
for _ in range(M):
  problem, result = input().split()
  if results[int(problem)] == 0 and result == 'AC':
    ac_cnt += 1
    results[int(problem)] = 1
  elif results[int(problem)] == 0 and result == 'WA':
    wa_list[int(problem)] += 1
for i in range(1, N+1):
  if results[i] == 1:
    wa_cnt += wa_list[i]
print(ac_cnt, wa_cnt)
