k = int(input())
a = list(map(int,input().split()))

def check(n):
    for i in a:
        n = n//i*i
    return n

bot=top=0

# 2以上最小値
l = 0
r = sum(a)+2
while r-l>1:
    mid = (l+r)//2
    if check(mid) >1:
        r = mid
    else:
        l = mid
bot = r

# 2以下最大値
l = 0
r = sum(a)+2
while r-l>1:
    mid = (l+r)//2
    if check(mid) < 3:
        l = mid
    else:
        r = mid
top = l
if bot <= top:
    print(bot, top)
else:
    print(-1)