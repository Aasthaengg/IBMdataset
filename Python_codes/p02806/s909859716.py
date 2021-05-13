# 標準入力
N = int(input()) #1行目のNを取得する
#s = [input() for i in range(N+1)] #複数行の数値の入力を取得
s = [list(map(str, input().split())) for i in range(N+1)]
# print(N)
# print(s)
list_music = []
list_time = []
sleep_music = s[N]
# print(sleep_music[0])

for i in range(N):
    for j in range(2):
        # print(s[i][j])
        if j == 0:
            list_music.append(s[i][j])
        elif j == 1:
            list_time.append(int(s[i][j]))

# print("タイトル：" + str(list_music))
# print("時間：" + str(list_time))

sleep_point = list_music.index(sleep_music[0])
# print((sleep_point))
sleep_time = 0
for i in range(sleep_point+1, N):
    # print(i)
    sleep_time += list_time[i]

# sleep_time = sum(int(list_time) for i in range(sleep_point+1, N))
# sleep_time = sum(int(i) for i in list_time(range(sleep_point+1, N)))
print(sleep_time)