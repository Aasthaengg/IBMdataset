from math import ceil
n,h = map(int,input().split())
a,b = [],[]
for _ in range(n):
    a_,b_ = map(int,input().split())
    a.append(a_)
    b.append(b_)
mx_a = max(a)
b.sort(reverse=True)
cnt = 0
tmp = 0
for b_ in b:
    if b_ >= mx_a:
        tmp += b_
        cnt += 1
        if tmp >= h:
            print(cnt)
            exit()
    else:
        break
print(cnt+ceil((h-tmp)/mx_a))