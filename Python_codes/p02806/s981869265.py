n = int(input())
song_list = [input().split() for _ in range(n)]
last_song = input()

count = 0
flag = False

for song in song_list:
    if flag == True:
        count += int(song[1])
    elif song[0] == last_song:
        flag = True

print(count)