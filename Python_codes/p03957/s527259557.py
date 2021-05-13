# h,w=map(int,input().split())
s=input()

flag=False
for i in range(len(s)):
    if s[i] == 'C':
        for j in range(i,len(s)):
            if s[j]=='F':
                flag=True
print('Yes' if flag else 'No')
