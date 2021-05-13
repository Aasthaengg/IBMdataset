n = int(input())
s = input()

wn = s.count('.')
bn = n - wn
ans = min(wn,bn)

lw = 0
lb = 0
for i in range(n):
  if s[i]=='.':
    lw += 1
  else:
    lb += 1      
  ans = min(ans, lb + (wn - lw))
  
print(ans)