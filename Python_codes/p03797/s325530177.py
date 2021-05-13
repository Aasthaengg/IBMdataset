s, c = map(int, input().split())
if c/2 > s:
  c -= s*2
  scc = s + c//4
else:
  scc = c//2
print(scc)