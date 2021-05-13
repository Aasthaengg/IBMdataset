#coding:utf-8
ans = [0] * 4

for i in range(3):
  a, b = map(int, input().split())
  ans[a-1] += 1
  ans[b-1] += 1
  
for i in ans:
  if i >= 3:
    print("NO")
    exit()

print("YES")
  
