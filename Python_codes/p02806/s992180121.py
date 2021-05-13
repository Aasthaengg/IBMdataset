n = int(input())
playlist = []
for _ in range(n):
    playlist.append(input().split())

x = input()

ans = 0
flg = False
for play in playlist:
    if flg:
        ans += int(play[1])
    if play[0] == x:
        flg = True

print(ans)