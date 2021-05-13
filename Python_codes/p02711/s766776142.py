n=str(input())
cnt=0
for i in range(3):
    if n[i]=='7':
        cnt+=1
if cnt>=1:
    print('Yes')
else :
    print('No')
