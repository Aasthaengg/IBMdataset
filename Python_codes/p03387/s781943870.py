num = list(map(int,input().split()))
num.sort(reverse=True)
M = max(num)
l = [M-i for i in num]
gap = l[2] - l[1]
ans = 0

if gap % 2 == 0:
    ans = l[1] + int(gap/2)
else:
    ans = l[1] + int(gap/2)+2
print(ans)