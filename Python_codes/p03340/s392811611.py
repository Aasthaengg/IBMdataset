n=int(input())
a=list(map(int,input().split()))
j=0
c=0
s=a[0]
for i in range(n):
    if j<i:
        j=i
        s=a[i]
    if j<n-1:
        while s&a[j+1]==0:
            s|=a[j+1]
            j+=1
            if j==n-1:
                break
    c+=j-i+1
    s^=a[i]
print(c)