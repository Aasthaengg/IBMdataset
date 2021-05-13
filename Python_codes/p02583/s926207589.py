n = int(input())
l = list(map(int,input().split()))
count = 0
l.sort()
for a,i in enumerate(l):
    for b,j in enumerate(l,a+1):
        if i >= j:
            continue
        for c,k in enumerate(l,b+1):
            if j >= k:
                continue
            if k-j<i:
                count+=1
                
print(count)