n = int(input())
worklist = []
for i in range(n):
    alist=list(map(int,input().split()))
    worklist.append(alist)

worklist.sort(key=lambda x: x[1])
timecount = 0
count = 0

for i in range(n):
    timecount += worklist[i][0]
    if timecount > worklist[i][1]:
        count += 1

if count == 0:
    print('Yes')
else:
    print('No')