h,w = map(int, input().split())

Ans = []
for i in range(h):
  list = input()
  Ans.append(list)
  Ans.append(list)

for i in range(h):
  print(Ans[2*i])
  print(Ans[2*i+1])