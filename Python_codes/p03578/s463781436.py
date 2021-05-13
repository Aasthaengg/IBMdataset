import collections

n = int(input())
dd = list(map(int, input().split()))
m = int(input())
tt = list(map(int, input().split()))
cd = collections.Counter(dd)
ct = collections.Counter(tt)

if m > n:
  print('NO')
  exit()
        
for t in ct: 
  if ct[t] <= cd[t]:
    continue
  else:
    print('NO')
    exit()
print('YES')
