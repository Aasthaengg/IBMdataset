s = input()+'R'
ans = [0]*(len(s)-1)
a = 0
b = 0
cnt = 0
for i in s:
  if i=='L' and b==0:
    b = cnt
  if b!=0 and i=='R':
    ans[b-1] = 1+(b-1-a)//2+(cnt-b)//2
    ans[b] = 1+(b-a)//2+(cnt-1-b)//2
    a = cnt
    b = 0
  cnt+=1
print(' '.join(map(str,ans)))