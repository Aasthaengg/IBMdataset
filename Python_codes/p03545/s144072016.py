lsnum = list(input())
lsnum1 = [int(i) for i in lsnum]
ls = ['+','-']
for i in range(2 ** 3):
    ans = lsnum1[0]
    for j in range(3):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
           ans += lsnum1[j+1]
        else:
            ans -= lsnum1[j+1]
    if ans == 7:
        bit = i
        break
ans2 = lsnum[0]
for i in range(3):
    if ((bit >> i) & 1):
        ans2 += '+'+lsnum[i+1]
    else:
        ans2 += '-'+lsnum[i+1]
print(ans2+'=7')