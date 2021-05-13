from collections import Counter
n = int(input())
A = list(map(int, input().split()))
counter = Counter(A)
work = []
temp = []
for k, v in sorted(counter.items(), key=lambda x:x[0], reverse=True):
    if v >= 4:
        temp.append(k)
    if v >= 2:
        work.append(k)
        if len(work)==2:
            break   
if len(work) < 2:
    if len(temp)==0:
        result = 0
    else:
        result = temp[0]**2
else:
    if len(temp)==0:
        result = work[0]*work[1]
    else:
        result = work[0]*work[1] if work[0]*work[1]>temp[0]**2 else temp[0]**2
print(result)