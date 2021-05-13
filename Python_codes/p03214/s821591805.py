n=int(input())
a=list(map(int,input().split()))
ave=sum(a)/n
for i in range(n):
    a[i]=max(a[i]-ave,ave-a[i])
min=min(a)
for i in range(n):
    if a[i]==min:
        print(i)
        exit()
 
