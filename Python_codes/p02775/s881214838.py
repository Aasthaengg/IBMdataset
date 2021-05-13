#E 復習
N = list(input())
N = [int(n) for n in N]
N.insert(0, 0)
len_N = len(N)
ans = 0

for i in reversed(range(len_N)):
    num = int(N[i])
    if num == 10:
        N[i-1] += 1
    #他の人の回答をみて、足りなかったのはここの処理。なぜ必要なのか調べる。
    elif num==5:
        if int(N[i-1])>=5:
            ans += 5
            N[i-1] += 1
        else:
            ans += 5
    ###################################
    elif num >5:
        ans += (10-num)
        N[i-1] += 1
    else:
        ans += num

print(ans)