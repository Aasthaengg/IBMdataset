#from collection import deque
N, K, C = map(int, input().split())
C += 1
S = input()

DP = [-1 for _ in range(N)] #i日目から初めて、働くことのできる最大の回数

day_prv = [-1] #その日からc日目後に働くことのできた日(day_prv[-c])
for day in range(N-1, -1, -1):
  if S[day] == "x": 
    day_prv.append(day_prv[-1])
  else:
    if day + C >= N or day_prv[-C] == -1:
      DP[day] = 1
    else:
      DP[day] = DP[day_prv[-C]] + 1
    day_prv.append(day) 
  #print(day, day_prv, DP)
  
if DP[0] == K:
  val = DP[0]
  day_start = 0
  ct = 0
  while day_start < N:
    day = day_start
    while day < N and DP[day] != val-1:
      if DP[day] == val:
        ct += 1
      day += 1 
      #print(day, ct)
    if ct == 1:
      print(day_start+1)
    day_start = max(day, day_start + C)
    while day_start < N and DP[day_start] == -1:
      day_start += 1  
    #print(day, ct, val, day_start)
    ct = 0
    val -= 1

