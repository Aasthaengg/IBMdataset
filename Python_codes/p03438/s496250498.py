n = int(input())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
# 大きい順 or 小さい順に揃えていく
ds = [a-b for a,b in zip(As,Bs)]
if sum(ds) > 0:
    print("No")
    exit()
cnt = 0
cnts = []
for d in ds:
    # print(d)
    if d < 0:
        c = -(d//2)
        cnt += c
        d += c * 2
    cnts.append(d)
if cnt >= sum(cnts):
    print("Yes")
else:
    print("No")