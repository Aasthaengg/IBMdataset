n = int(input())
l = list(map(int,input().split()))

if l[0] <= 0:
    x = 1
    ans1 = 1-l[0]
else:
    x = l[0]
    ans1 = 0
def check(l,x):
    ans=0
    for i in range(1,n):
        if x < 0:
            if x + l[i] <= 0:
                ans += 1-(x+l[i])
                x = 1
            else:
                x = x + l[i]
        else:
            if x + l[i] >= 0:
                ans += x + l[i] + 1
                x = -1
            else:
                x = x + l[i]
    return ans
ans1 += check(l,x)
if l[0] >= 0:
    x = -1
    ans2 = l[0]+1
else:
    ans2 = 0
    x = l[0]
ans2 += check(l,x)
print(min(ans1,ans2))
