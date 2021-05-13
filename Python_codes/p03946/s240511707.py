n,t = map(int,input().split())
A = list(map(int,input().split()))
A_rev = A[::-1]
tmp_max = []
for i, a in enumerate(A_rev):
    if i==0:
        tmp_max = [A_rev[i]]
    else:
        tmp_max += [max(A_rev[i], tmp_max[-1])]
buy = [max(0, x-y) for x,y in zip(tmp_max[::-1], A)]
x = max(buy)
cnt = 0
for b in buy:
    if b==x:
        cnt += 1
print(cnt)