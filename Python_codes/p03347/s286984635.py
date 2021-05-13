N = int(input())
A = [int(input()) for _ in range(N)]

#先頭は増やせないから０以外なら終わり
if A[0] != 0:
    print(-1)
    exit()


ans = 0
prev = 0
for n in reversed(A):
    if prev != 0:
        # 後ろから見て１ずつ減少する場合
        if n == prev - 1:
            prev = n
        # 前以上のとき、新たにその数字のために階段を構成する（前の数字を作る仮定で作れない）ので、その分の操作数が必要
        elif n >= prev:
            ans += n
            prev = n
        # ２以上の差があると作れない
        else:
            print(-1)
            exit()
    else:
        ans += n
        prev = n


print(ans)
