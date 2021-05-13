N = int(input())

cnt = 0
A = 0
B = 0
AB = 0

for _ in range(N):
  s = input()
  if s[0] == 'B':
    B += 1
  if s[-1] == 'A':
    A += 1
  if s[-1] == 'A' and s[0] == 'B':
    AB += 1
  for i in range(len(s)-1):
    if s[i] == 'A' and s[i+1] == 'B':
      cnt += 1
    
cnt += min(A,B)
if A == AB and B == AB and AB > 0:
  cnt -= 1
  
print(cnt)