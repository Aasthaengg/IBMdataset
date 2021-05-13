n = int(input())
S = [None] * n
T = [None] * n
for i in range(n):
    S[i], T[i] = input().split()
x = input()
sleep_song_index = S.index(x)

counter = 0
for i in range(sleep_song_index+1, n):
    counter += int(T[i])
print(counter)