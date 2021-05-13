s = input()
ans= 0
a = 'CODEFESTIVAL2016'
for ss,aa in zip(s,a):
  if ss != aa:
    ans += 1
print(ans)