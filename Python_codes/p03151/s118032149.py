N = int(input())
A = list(map(int, input().split())) # 現準備度
B = list(map(int, input().split())) # 必要準備度

if sum(A) < sum(B):
    print(-1)
else:
    minus = 0
    plus_list = []
    ans = 0
    for a, b in zip(A, B):
        if a - b < 0:
            ans += 1
            minus += b - a
        elif a - b > 0:
            plus_list.append(a - b)

    plus_list.sort(reverse=True)
    for p in plus_list:
        if minus <= 0:
            break
        ans += 1
        minus -= p
    if minus > 0:
        print(-1)
    else:
        print(ans)
