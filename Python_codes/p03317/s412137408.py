n,k = map(int,input().split())
a = list(map(int,input().split()))

for i_1 in range(n):
    if a[i_1]==1:
        break

#print(i_1)
#print(a[:i_1],a[i_1+1:])
if len(a[:i_1])==0:
    ans = len(a[i_1+1:])//(k-1)
    if len(a[i_1+1:])%(k-1)==0:
        print(ans)
    else:
        print(ans+1)
elif len(a[i_1+1:])==0:
    ans = len(a[:i_1])//(k-1)
    if len(a[:i_1])%(k-1)==0:
        print(ans)
    else:
        print(ans+1)
else:
    ans = len(a[:i_1])//(k-1) + 1
    tmp = ans * (k-1)
    ans += len(a[tmp+1:])//(k-1)
    if len(a[tmp+1:])%(k-1)==0:
        print(ans)
    else:
        print(ans+1)
