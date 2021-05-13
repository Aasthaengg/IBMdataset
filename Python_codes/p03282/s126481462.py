import sys
s=input()
k=int(input())
for i in range(min(len(s),k)):
  if s[i]!='1':
    print(s[i])
    sys.exit()
print(1)