n=int(input())
a=[int(input()) for i in range(n)]
count=0

if a[0]!=0: count=-1
else:
    for i in range(n-1):
        if a[i]+1==a[i+1]:
            count+=1
        elif a[i]+1<a[i+1]:
            count=-1
            break
        else:
            count+=a[i+1]
print(count)