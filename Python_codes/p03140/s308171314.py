n=int(input())
a=list(reversed(list(input())))
b=list(reversed(list(input())))
c=list(reversed(list(input())))
ans=0
for i in range(n):
    if a[i]==b[i] and b[i]==c[i]:
        continue
    elif a[i]==b[i] or b[i]==c[i] or c[i]==a[i]:
        ans+=1
    else:
        ans+=2
print(ans)
