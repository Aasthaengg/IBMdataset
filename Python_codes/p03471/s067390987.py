n, y = map(int, input().split())

total = 0
ans = list()
for a in range(0, n+1, 1):
  for b in range(0, n+1, 1):
    if a + b <= n:
      c = n - (a+b)
      total = a*10000 + b*5000 + c*1000
      if total == y:
        lists = [a,b,c]
        ans.append(lists)
    else:
      break

if ans == []:
  answer = ['-1', '-1', '-1']
  answer = ' '.join(answer)
else:
  answer = [str(i) for i in ans[0]]
  answer = ' '.join(answer)

print(answer)