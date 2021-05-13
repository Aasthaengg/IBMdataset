n=input()
ans=0
for i in n:
    if i=='9':
        ans+=1
print('Yes' if ans>0 else 'No')
