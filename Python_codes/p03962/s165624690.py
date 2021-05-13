l=list(map(int,input().split()))
tmp = []
count=0
for i in l:
    if not i in tmp:
        count+=1
        tmp.append(i)
print(count)