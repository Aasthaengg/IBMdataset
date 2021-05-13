N = int(input())
As = list(map(int,input().split()))
counts = []
now = As[0]
count = 1
for a in range(1,len(As)):
    if As[a]==now:
        count+=1
        if a == len(As)-1:
            counts.append(count)
    else:
        counts.append(count)
        count =1
        now = As[a]
print(sum([i//2 for i in counts]))