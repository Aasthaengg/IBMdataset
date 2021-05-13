n=int(input())
a=list(map(int,input().split(' ')))
x=0
y=0
a.sort()
a.reverse()
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        x=a[i]
        p=i+1
        break
if x!=0:
    for i in range((p+1),len(a)-1):
        if a[i]==a[i+1]:
            y=a[i]
            break
print(x*y)