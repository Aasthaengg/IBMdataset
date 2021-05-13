N = int(input())
D = list(map(int, input().split()))
assert len(D) == N

# i個目のたこ焼のうまさDi
# おいしさがx,yのたこやき2個を食べると体力がxy回復
total = 0
for i,x in enumerate(D[:-1]):
  for y in D[i+1:]:
    total += x * y
print(total)