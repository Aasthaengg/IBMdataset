s=list(input())
t=list(input())
flag=0
if s==t:
    flag=1
for i in range(len(s)):
    s.insert(0,s[-1])
    s.pop(-1)
    if s==t:
        flag=1
if flag==1:
    print('Yes')
else:
    print('No')