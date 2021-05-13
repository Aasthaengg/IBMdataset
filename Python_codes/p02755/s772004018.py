import math
a,b = [float(i) for i in input().split()]
ans = 1000000000
flag = False

for i in range(1,1005):
    ans8 = int(math.floor(i*0.08))
    ans10 = int(math.floor(i*0.1))
#     print(ans8,ans10)
    if ans8 == a and ans10 == b:
        ans = min(ans, i) # 更新する必要がある．
        flag = True

if flag is True:
    print(ans)
else:
    print(-1)