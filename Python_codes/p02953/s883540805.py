n,*h=map(int,open(0).read().split())

cur=0
for height in h:
    if cur>height:
        print('No')
        exit(0)
    
    if cur==height:
        continue

    cur=height-1

print('Yes')