n=int(input())
s=list(map(int,input().split()))
cc=[]
ans=s[0]
for i in range(1,n):
    ans^=s[i]
if ans==0:
    print('Yes')
else:
    print('No')
