n = int(input())
songs = []
subs_total = 0
total = 0
for _ in range(n):
    s, t = input().split()
    total += int(t)
    songs.append([s,t])
x = input()
for i in range(n):
    subs_total += int(songs[i][1])
    if songs[i][0] == x:
        break
ans = total - subs_total
print(ans)