n=int(input())
l=list(map(int,input().split()))
d=[l[0]]
for i in range(n-1):
    if(l[i]>=l[i-1]):
        d.append(l[i])
    else:
        d[i]=l[i]
        d.append(l[i])
print(sum(d))
