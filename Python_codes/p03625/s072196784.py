from collections import Counter
n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
t = 4
s = []
for i in sorted(count.items(), key=lambda x: x[0], reverse=True):
  if i[1] >= 4 and t == 4:
    print(i[0]**2)
    exit()
  if i[1] >= 2 and t != 0:
    t -= 2
    s.append(i[0])
  elif t == 0: break
    
if len(s) != 0: print(s[0]*s[1])
else: print(0)