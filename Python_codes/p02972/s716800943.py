n = int(input())
a = list(map(int,input().split()))
b = [0]*n
for i in range(n):
    b1=b[n-1-i::n-1-i+1]
    su=sum(b1)
    if (a[n-1-i]==0 and su%2==0) or (a[n-1-i]==1 and su%2==1):
        b[n-1-i]=0
    else:
        b[n-1-i]=1
ans =[]
print(sum(b))
for i in range(n):
    if b[i]==1:
        ans.append(str(i+1))
print(' '.join(ans))
