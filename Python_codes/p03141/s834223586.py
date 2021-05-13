n=int(input())
a,b=[0]*n,[0]*n
s=[[0 for i in range(2)] for j in range(n)]
for i in range(n):
    a[i],b[i]=map(int,input().split())
    s[i][0]=a[i]+b[i]
    s[i][1]=i
s.sort(reverse=True)
s1=0
s2=0
for i in range(n):
    if i%2==0:
        s1+=a[s[i][1]]
    else:
        s2+=b[s[i][1]]
print(s1-s2)
