import sys
readline = sys.stdin.readline

# 現在のインデックスを持ちながらBFSしてみよう

N = int(readline())
S = readline().rstrip()

from collections import deque
q = deque([])

for i in range(10):
  q.append(["",0,str(i)])
  
ans = 0
while q:
  # 現在の文字列、探し始めるインデックス、探している文字列
  num, ind, target = q.popleft()
  while ind < len(S):
    if S[ind] == target:
      break
    ind += 1
  else:
    continue
  num += target
  if len(num) == 3:
    ans += 1
    continue
  for i in range(10):
    q.append([num, ind + 1, str(i)])

print(ans)