x = int(input())
#6,5,6,5...で何回加算されていくか。
#余りの部分は後で処理
ans = x // 11 * 2

if x % 11 > 6:
    print(ans + 2)
elif x % 11 > 0:
    print(ans + 1)
else:
    print(ans)#余りなし=割り切れる時
