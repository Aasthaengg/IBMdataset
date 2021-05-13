# coding: utf-8
# Your code here!
s=list(input())
count=0

for i in range(len(s)):#偶数ならグー　奇数ならパーになる
    if s[i]=='g':
        s[i]=0
    else:
        s[i]=1
    if i&1^s[i]==1 and i&1==1:
        count+=1
    elif i&1^s[i]==1 and s[i]&1==1:
        count-=1
    else:
        pass

print(count)
