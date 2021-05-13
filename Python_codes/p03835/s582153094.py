k,s = map(int,input().split())
k=k+1
count=0
for i in range(k):
    for j in range(k):
        if i+j > s:
            break
        m = s - (i+j)
        if m >= 0 and m < k:
            count = count+1
        #print(i," ",j," ",m)

print(count)