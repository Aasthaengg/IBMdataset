import bisect
q = int(input())
LR = (tuple(map(int,input().split())) for i in range(q))
ans = []
sosuu = [2]
A = 100000
for L in range(3, A, 2): # 2 以外の素数は奇数なので
    for L2 in sosuu:
        if L % L2 == 0:
            break # 素数でないことがわかったらそれ以上ループする必要はない
    else: # break で抜けることがなかったら L は素数（Python 特有の制御構文）
        sosuu.append(L)
        if (L+1)/2 in sosuu:
          ans.append(L)
for lr in LR:
  print(bisect.bisect_right(ans,lr[1]) - bisect.bisect_left(ans,lr[0]))