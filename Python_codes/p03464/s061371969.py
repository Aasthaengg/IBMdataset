k = int(input())
a = list(map(int,input().split()))
def cal(x):
    for i in range(k):
        x -= (x%a[i])
    return x
top = 3+ k*max(a)
bot = 0
while top - bot > 1:
    mid = (top+bot)//2
    if cal(mid) >= 2:top = mid
    else:bot = mid
mini = top
top = 3+ k*max(a)
bot = 0
while top - bot > 1:
    mid = (top+bot)//2
    if cal(mid) > 2:top = mid
    else:bot = mid
maxi = bot
if mini > maxi:print(-1)
    
else:print(mini,maxi)
