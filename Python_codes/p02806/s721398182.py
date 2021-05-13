length_of_input = int(input())

playlist = []
for i in range(length_of_input):
    current_line_list = input().split()
    playlist.append({"title": current_line_list[0], "length": int(current_line_list[1])})

last_awake_title = input()

duration_of_sleep = 0
sleeping_flag = False

for music_obj in playlist:
    if sleeping_flag:
        duration_of_sleep += music_obj["length"]
    else:
        if music_obj["title"] == last_awake_title:
            sleeping_flag = True

print(duration_of_sleep)