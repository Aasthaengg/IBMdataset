N, M = map(int, input().split())
S = input()

steps = [[] for i in range(N+1)]
steps[0] = [0]
num_steps = 0
root = [0] + [-1]*N
pos = 1

while pos <= N:
  starts = steps[num_steps]
  if not starts:
    break
  for start in starts:
    end = min(start+M+1, N+1)
    for i in range(pos, end):
      if S[i] == '0':
        steps[num_steps+1].append(i)
        root[i] = start
    
    pos = end
  
  num_steps += 1


if root[N] == -1:
  ans = -1
else:
  pos = N
  ans = []
  while pos > 0:
    pre_pos = root[pos]
    ans.append(str(pos - pre_pos))
    pos = pre_pos
  
  ans = ans[::-1]
  ans = ' '.join(ans)


print(ans)