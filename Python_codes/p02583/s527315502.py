n=int(input())
l=list(map(int,input().split()))
if n<=2:
    print(0)
else:
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if l[i]!=l[j] and l[j]!=l[k] and l[k]!=l[i]:
                    a=[l[i],l[j],l[k]]
                    a.sort()
                    if a[2]<a[0]+a[1]:
                        count+=1
    print(count)