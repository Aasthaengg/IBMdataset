N = int(input())
song_title = []
song_len = []
for i in range(N):
    t, l = input().split()
    song_title.append(t)
    song_len.append(int(l))


X = input()
last = 0
for i in range(N):
    if song_title[i] == X:
        last = i
        break

ans = 0
for i in range(last + 1, N):
    ans += int(song_len[i])
print(ans)