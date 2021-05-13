s = input()
t = input()
cnt = 0
for i, p in enumerate(s):
  if p != t[i]:
    cnt += 1
    
print(cnt)
