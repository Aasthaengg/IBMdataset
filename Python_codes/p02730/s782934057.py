s=input()
n=len(s)
n1=(n-1)//2
n2=(n+3)//2
s1=s[:n1]
s2=s[n2-1:]

for i in range(1,n1+1):
    if s[i-1]!=s[-i]:
        print('No')
        exit()
for i in range(1,n1//2+1):
    if s1[i-1]!=s1[-i]:
        print('No')
        exit()
print('Yes')