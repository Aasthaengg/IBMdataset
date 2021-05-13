price, poket_money, max_music = map(int, input().split())

music_times = -1
for i in range(0, poket_money + 1, price):
    music_times += 1
    if max_music == music_times:
        break

print(music_times)