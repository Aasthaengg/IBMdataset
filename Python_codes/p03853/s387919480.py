h, w = map(int, input().split())

ans = []
for _ in range(h):
  c = input()
  for _ in range(2):
    ans.append(c)
    
for a in ans:
  print(a)