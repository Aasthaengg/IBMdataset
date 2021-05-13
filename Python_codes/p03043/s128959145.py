#n = int(input())
import math
n, k = map(int, input().split())
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(h)]

ans = 0

for i in range(1, n+1):
    if i>=k:
        heads_num=0
    else:
        heads_num = math.ceil(math.log2(k/i))
    add = (1/n)*((0.5)**heads_num)
    ans += add
    #ans += (1/n)*((0.5)**heads_num)

print('{:.12f}'.format(ans))
