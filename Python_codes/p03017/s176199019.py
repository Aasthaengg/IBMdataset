n,a,b,c,d = map(int,input().split())
s = input()
a,b,c,d = a-1,b-1,c-1,d-1
if s[a:c+1].count('##') > 0 or s[b:d+1].count('##') >0:
  print('No')
  exit()
if c > d:
  if s[b-1:d+2].count('...') == 0:
    print('No')
    exit()
print('Yes')