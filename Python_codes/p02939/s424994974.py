s = input()
prev = ""
current = ""
cnt = 0
for i in s:
  current += i
  if current!=prev:
    cnt+=1
    prev = current
    current = ""
print(cnt)