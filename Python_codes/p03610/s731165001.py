s = input()
ans = []
for i,si in enumerate(s):
  if i%2 == 0:
    ans.append(si)
print(''.join(ans))
