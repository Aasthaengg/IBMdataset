import collections

N = int(input())
rates = list(map(int, input().split()))

colors = [min(8, i // 400) for i in rates]
CTR_colors = collections.Counter(colors)

ans = len(CTR_colors)

if (CTR_colors[8] > 0):
    ans -= 1

    if (ans == 0):
        mini_ans = ans + 1
    else:
        mini_ans = ans
    
    max_ans = min(100, ans + CTR_colors[8])

else:
    mini_ans, max_ans = ans, ans

print(mini_ans, max_ans)
