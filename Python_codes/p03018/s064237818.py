S = input()
S = S.replace('BC', 'D')
S = S.replace('B', 'C')
S = S.split('C')
ans = 0

def count_inv(s):
  res = num = 0
  for si in s:
    if si == 'A':
      num += 1
    else:
      res += num
  return res


for s in S:
  ans += count_inv(s)
  
print(ans)