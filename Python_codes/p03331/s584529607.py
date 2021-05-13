n = int(input())
ans = 10**10
for i in range(1,n):
    j = n-i
    l1 = len(str(i))
    l2 = len(str(j))
    l1_cnt,l2_cnt = 0,0
    for k in range(l1):
        l1_cnt +=int(str(i)[k])
    for l in range(l2):
        l2_cnt +=int(str(j)[l])
    ans = min(ans,l1_cnt+l2_cnt)
print(ans)