n = int(input())
s = input()
i = 0
cnt = 0
while i < n:
  if s[i:i+3] == 'ABC':
    cnt += 1
    i += 3
  else:
    i += 1
print(cnt)