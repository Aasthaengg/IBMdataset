#sig49san
N = int(input())
alpha_list = "abcdefghijklmnopqrstuvwxyz"
ans = ""
moji_list = []
while(N != 0):
    tmp = N % 26
    if(tmp == 0):
        tmp = 26
    moji_list.append(alpha_list[tmp-1])
    N = (N - tmp) // 26
for hoge in reversed(moji_list):
    ans += hoge
print(ans)
