a=input()
ans=int()
for i in range(len(a)):
    if 'C' in a[i]:
        b=a[i+1:]
        for j in range(len(b)):
            if 'F' in b[j]:
                ans+=1
print('Yes' if ans>0 else 'No')