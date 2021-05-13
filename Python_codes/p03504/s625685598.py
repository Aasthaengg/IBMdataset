from itertools import accumulate
import sys
input = sys.stdin.readline
N,C = map(int,input().split())
p = [list(map(int,input().split())) for i in range(N)]
p.sort()
ch = [[0,0] for i in range(C+1)]
p_true = []
for i in range(N):
  [s,t,c] = p[i]
  if ch[c][1] == s:
    ch[c][1] = t
  elif ch[c] == [0,0]:
    ch[c] = [s,t]
  else:
    p_true.append([ch[c][0],ch[c][1],c])
    ch[c] = [s,t]
for i in range(1,C+1):
  if ch[i] != [0,0]:
    p_true.append([ch[i][0],ch[i][1],i])
p_true.sort()
time = [0 for i in range(100002)]
for i in range(len(p_true)):
  [s,t,c] = p_true[i]
  time[s] += 1
  time[t+1] -= 1
print(max(accumulate(time)))