n=int(input())
a=list(map(int,input().split()))
count=0
i=1
while i<len(a)-1:
    if (a[i]>a[i+1] and a[i]<a[i-1]) or (a[i]<a[i+1] and a[i]>a[i-1]):
        count+=1
    i+=1
print(count)