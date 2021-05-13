n = int(input())
l = []
for i in range(n):
    tmp = list(map(int,input().split()))
    l.append(tmp)

if len(l) == 1:
    print(1)
    exit()


from collections import defaultdict
d = defaultdict(int)

for i in range(len(l)):
    for j in range(len(l)):
        difx = l[i][0] - l[j][0]
        dify = l[i][1] - l[j][1]
        if difx!=0 or dify!=0:
            dif = str(difx) + "_" + str(dify)
            d[dif] += 1

p_q = max((v,k) for (k,v) in d.items())[1]
p,q = p_q.split("_")

ans=0
for i in range(len(l)):
    found=False
    for j in range(len(l)):
        difx = l[i][0] - l[j][0]
        dify = l[i][1] - l[j][1]
        if difx==int(p) and dify==int(q):
            found=True
            break
    if not found:
        ans+=1
print(ans)