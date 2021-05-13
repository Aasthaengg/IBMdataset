n=int(input())
k=int(input())
c=0
s=list(map(int,input().split()))
for i in range(n):
    if s[i]>k-s[i]:
        c+=(k-s[i])*2
    else:
        c+=s[i]*2
print(c)