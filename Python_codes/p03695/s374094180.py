N = int(input())
a = list(map(int, input().split()))
ans = [0]*9
for i in a:
    if i < 400: ans[0] = 1
    elif i < 800: ans[1] = 1
    elif i < 1200: ans[2] = 1
    elif i < 1600: ans[3] = 1
    elif i < 2000: ans[4] = 1
    elif i < 2400: ans[5] = 1
    elif i < 2800: ans[6] = 1
    elif i < 3200: ans[7] = 1
    else: ans[8] += 1
print(max(sum(ans[:8]), 1), sum(ans[:8])+ans[-1])

