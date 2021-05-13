#list(map(int, input().split()))
s=input()
b=0
for i in range(len(s)):
    if s[i] == 'C':
        for j in range(i+1,len(s)):
            if(s[j]=='F'):b=1
print('Yes')if b else print('No')