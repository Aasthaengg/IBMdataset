n = int(input())
a = [-1]
a.extend(list(map(int, input().split())))
cnt = 0
ansID = []
ans = [-1]*(n+1)

for i in reversed(range(1, len(a))):
  tmp = a[i]
  j = i*2
  while j < len(ans):
    tmp += ans[j]
    j += i
  ans[i] = tmp%2
  cnt += tmp%2
  if tmp%2 == 1:
    ansID.append(i)
  
print(cnt)
for ans in ansID:
  print(ans, end=" ")
