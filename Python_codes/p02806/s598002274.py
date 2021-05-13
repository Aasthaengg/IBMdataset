N = int(input())
songs = []
times = []
for _ in range(N):
  song,time = input().split()
  songs.append(song)
  times.append(int(time))
start = input()
number = songs.index(start)
if number == len(songs):
  print(0)
else:
  print(sum(times[number+1:]))