n = int(input())
s = list(map(int,input().split()))
prev = 0
ch = 0
for c in s:
  if prev == c:
    ch += 1
    prev = 0
  else:
    prev = c
print(ch)