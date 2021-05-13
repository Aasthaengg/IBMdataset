from collections import deque
n,power = map(int,input().split())
swing_ls = [0] * n
throw_ls = [0] * n
for i in range(n):
    swing, throw = map(int,input().split())
    swing_ls[i] = swing
    throw_ls[i] = throw
swing_best = max(swing_ls)
throw_ls.sort(reverse=True)
def isOK(index, key, l):
    if l[index] <= key:
        return True
    else:
        return False
def meguru_search(l, key):
    '''
    key以上の値を持つ最小のインデックスを返す
    '''
    left = -1
    right = len(l)

    while (right - left) > 1:
        mid = left + (right - left) // 2
        # 直感的に記憶　
            # 「含まれている」んだったら「含むを許容（等号付き）する右側」はmidまで動かして問題ない
                # 新しいrightの位置がkeyの位置だとしても、「含む」は許容されてる
            # 「含まれていない」んだったら「含まない(<)左の壁」をそこまで動かしてもkeyを通り過ぎることはない
        if isOK(mid, key, l):
            right = mid
        else:
            left = mid
    
    # whileを抜ける時、rightとleftは一個差で、かつkeyがrightの位置にある
    return right
last_ind = meguru_search(throw_ls, swing_best) - 1
if last_ind != -1:
    throw_use_q = deque(throw_ls[:last_ind+1])
else:
    throw_use_q = []
count = 0
while power > 0:
    if throw_use_q:
        point = throw_use_q.popleft()
        power -= point
    else:
        count += -(-power // swing_best)
        break
    count += 1
print(count)
