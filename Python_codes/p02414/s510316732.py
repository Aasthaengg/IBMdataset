lst1=[]
lst2=[]
lst3=[]
answer_lst=[]
n,m,l=(int(x) for x in input().split())
for a in range(n):
    child_lst1=[]
    for b in input().split():
        child_lst1.append(int(b))
    lst1.append(child_lst1)
for c in range(m):
    child_lst2=[]
    for d in input().split():
        child_lst2.append(int(d))
    lst2.append(child_lst2)
for e in range(l):
    child_lst3=[]
    for f in lst2:
        child_lst3.append(f[e])
    lst3.append(child_lst3)
for g in range(1,n+1):
    child_lst4=[]
    need_lst1=lst1[g-1]
    for h in range(1,l+1):
        value=0
        need_lst2=lst3[h-1]
        for i in range(1,m+1):
            value+=need_lst1[i-1]*need_lst2[i-1]
        child_lst4.append(value)
    answer_lst.append(child_lst4)
for ans in answer_lst:
    print(*ans)
