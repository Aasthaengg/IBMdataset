n,a,b = map(int,input().split())
mons=[0 for i in range(n)]
for i in range(n):
    mons[i] = int(input())

def can_defeat(n):
    global mons
    global a
    global b
    base = b*n
    sup = 0
    for m in mons:
        if m-base > 0:
            sup += (m-base)//(a-b)+min((m-base)%(a-b),1)
    if sup <= n:
        return True
    else:
        return False

def bin_search(eval_func,left,right):
    if right-left <= 2:
        for i in range(left,right+1):
            if eval_func(i):
                return i
    mid = (left+right)//2
    if eval_func(mid):
        return bin_search(eval_func,left,mid)
    elif eval_func(right):
        return bin_search(eval_func,mid,right)

print(bin_search(can_defeat,0,int(1e10)))