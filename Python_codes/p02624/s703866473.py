#D
n = int(input())
#約数の数を求める＞＞倍数であり、n以下であるものの総和を求める

ans = 0
for i in range(1, n + 1):
    #iの倍数の数を求める
    m = n // i
    #初項i:公差i:m項までの等比数列の和
    ans += m * (2 * i + i * (m - 1)) *0.5
print(int(ans))