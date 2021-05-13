line =int(input())

data = [list(map(str,input().split()))for i in range(line)]

sleep_song = input()
sleep_time=0

for s in range(line):
  if data[s][0] ==sleep_song:
    sleep_moment =s+1
for t in range(sleep_moment,line):
  sleep_time +=int(data[t][1])
print(sleep_time)
