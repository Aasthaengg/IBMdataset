N = int(input())
music_list = [list(input().split()) for i in range(N)]
X = input()
switch = 0
time = 0
for i, j in music_list:
    if switch==1:
        time+=int(j)
    if i == X:
        switch=1
print(time)