from collections import defaultdict
d = defaultdict(int)
n = int(input())
for _ in range(n):
  a = input()
  g = [0]*26
  for i in a:
    g[ord(i)-97]+=1
  b = ''
  for i in g:
    b+=str(i)
  d[b]+=1
cnt = 0
for k,v in d.items():
  if v > 1:
    cnt += v*(v-1)//2
print(cnt)