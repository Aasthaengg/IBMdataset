n=int(input())
a=list(input())
b=list(input())
c=list(input())
ans=0
for i in range(n):
    if ( a[i] == b[i] and b[i] != c[i] ) or ( b[i] == c[i] and c[i] != a[i] ) or ( c[i] == a[i] and a[i] != b[i] ):
        ans+=1
    elif a[i] != b[i] and b[i] != c[i] and c[i] != a[i]:
        ans+=2
print(ans)
