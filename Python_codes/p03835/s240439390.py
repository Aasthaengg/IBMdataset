k,s = map(int, input().split())
count = 0
for a in range(k+1):
    for b in range(k+1):
        c = s-(a+b)
        if c>=0 and c<=k:
            count+=1
print(count)