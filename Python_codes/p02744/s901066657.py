import itertools
n = int(input())
#li = list(itertools.product([0,1], repeat=n))
alp = list('abcdefghijklmnopqrstuvwxyz')

ans_li = ['0']
for _ in range(n-1):
    tmp = []
    for a in ans_li:
        last = 0
        for an in a:
            if int(an)>last:
                last = int(an)
        for i in range(last+2):
            tmp.append(a+str(i))
    ans_li = tmp
for bb in ans_li:
    ans = ''
    for b in bb:
        ans += alp[int(b)]
    print(ans)