n=int(input())
s=input()
S=list(s)
S.sort()
count=0
if n==1:
    if S[0]=='B':
        print('No')
    else:
        print('Yes')
else:
    for i in range(n-1):
        if S[i]!=S[i+1]:
            count=i+1
            break
        if i==n-2:
            count=n-1
    if count>=(n+1)//2:
        print('No')
    else:
        print('Yes')