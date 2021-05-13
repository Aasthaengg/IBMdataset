import collections
s = list(input())
n = len(s)

cnt = [0,0,0]

for i in range(n):
  if s[i]=="a":
    cnt[0]+=1
  elif s[i]=="b":
    cnt[1]+=1
  else:
    cnt[2]+=1
    
print('YES' if max(cnt)-min(cnt) <= 1 else 'NO')
