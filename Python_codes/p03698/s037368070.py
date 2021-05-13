S = list(input())
r = 'yes'
for t in S:
  if S.count(t) > 1:
    r = 'no'
    break
print(r)