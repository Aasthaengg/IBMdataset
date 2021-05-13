from itertools import accumulate 

n = int(input())
song= []
time = [0]

for i in range(n):
    s, t = input().split()
    song.append(s)
    time.append(int(t) + time[i])

#time_acc = list(accumulate(time))
x = input()
print(time[n] - time[song.index(x) + 1])