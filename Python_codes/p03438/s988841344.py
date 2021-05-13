n = int(input())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))
delta = sum(li_b) - sum(li_a)
if delta < 0:
    print('No')
    exit()
elif delta == 0:
    if li_a == li_b:
        print('Yes')
        exit()
    else:
        print('No')
        exit()
else:
    li_d = []
    for i in range(n):
        li_d.append(li_b[i]-li_a[i])
    pa = 0
    pb = 0
    for i in li_d:
        if i >=0:
            pa += (i+1)//2
        else:
            pb += i
    if delta < max(pa, pb):
        print('No')
    else:
        print('Yes')