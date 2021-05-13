#!/usr/bin/env python3
import sys
input = sys.stdin.readline

n = int(input())
playlist = []

for i in range(n):
    s, t = input().split()
    playlist.append((s, t))
last_song = input().rstrip()

init = False
ans = 0
for title, time in playlist:
    if init:
        ans += int(time)
    if title == last_song:
        init = True

print(ans)