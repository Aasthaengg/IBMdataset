s = input().rstrip()
total = 0
for i in range(ord('a'),ord('z')+1):
  tmp = s.count(chr(i))
  total += tmp*(tmp-1)//2
print(1 + len(s)*(len(s)-1)//2 - total)