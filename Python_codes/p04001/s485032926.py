S = input()
N = len(S)
ans = 0
stack = [(0,0,1)]
while stack:
  t,s,g = stack.pop()
  if g >= N:
    ans+=t+int(S[s:g])
  else:
    stack.append((t,s,g+1))
    stack.append((t+int(S[s:g]),g,g+1))
print(ans)