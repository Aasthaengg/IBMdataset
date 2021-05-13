"""
多分またバグらせる
"""
# 尺取

N = int(input())
As = list(map(int, input().split()))
res = 0
l,r = 0, 0
val = As[l]
for l in range(N):
    cnt = 0
    # 区間が1のときは確定でOKなので+1する
    if l == r:
        r += 1
        val = As[l]
    # 差分が1以上(実質、区間が2つ以上存在するとき)
    elif r-(l-1) > 1:
        val -= As[l-1]
    # 条件を満たすうちは尺を伸ばす
    # print("be","l",l,"r",r,"val",val)
    while (r < N and val^As[r] == val+As[r]):
        val += As[r]
        r += 1
    # print("af","l",l,"r",r,"val",val)
    # 条件が終了したら差分を加える
    res += (r-l)
print(res)