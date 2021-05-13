import sys
s=list(input())
t=set(s)

r='abcdefghijklmnopqrstuvwxyz'

for i in range(26):
  if r[i] not in t:
    print(r[i])
    sys.exit()
    
print('None')