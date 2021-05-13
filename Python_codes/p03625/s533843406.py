from collections import Counter
n = int(input())
list_A = list(map(int, input().split()))
list_C = Counter(list_A)
list_D = sorted(list_C.items(), key=lambda x:x[0],reverse=True)
q = []
for i in range(len(list_D)):
    if len(q) == 2:
        break
    l = list_D[i]
    if l[1] > 1:
        q.append(l[0])
        if len(q) == 1 and l[1] > 3:
            q.append(l[0])
if len(q) == 2:
    print(q[0]*q[1])
else:
    print(0)