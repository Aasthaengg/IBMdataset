s = input()
w = int(input())
n = len(s)
ans = []
now = 0
while now<n:
  ans.append(s[now])
  now += w
for i in range(len(ans)):
  if i != len(ans)-1:
    print(ans[i],end='')
  else:
    print(ans[i])