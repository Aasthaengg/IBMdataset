S = input()

r2l = {'L': 'R', 'R': 'L'}
t = 'L'
ends = {'R': [], 'L': []}
for i, s in enumerate(S):
  if s == t:
    t = r2l[t]
    ends[t].append(i)

ends = []
ans = [0 for _ in range(len(S))]
cnt = 0
for i,s in enumerate(S):
  cnt += 1
  if s == t:
    if t == 'L':
      ans[i] = cnt // 2 + cnt % 2
      ans[i-1] = cnt // 2
      cnt = 0
      m = i
    t = r2l[t]
    cnt = 1
  elif t == 'R':
    if cnt % 2 == 0:
      ans[m-1] += 1
    else:
      ans[m] += 1
print(*ans)
  
#ans = [0 for _ in range(len(S))]
#current = 0
#e = ends['R'][current]
#ends['L'].append(len(S))
#print(ends)

t = 'R'
#m = e

#for i in range(len(S)):
#  if e < i and t == 'R':
#    t = r2l[t]
#    e = ends[t][current]
#  elif e <= i and t == 'L':
#    t = r2l[t]
#    current += 1
#    e = ends[t][current]
#    m = e
#  print(m)
#    
#  if abs(m - i) % 2 == 1:
#    ans[m-1] += 1
#  else:
#    ans[m] += 1