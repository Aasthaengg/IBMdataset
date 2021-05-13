n = int(input())
s = []
t = []

for _ in range(n):
    song, time = input().split()
    s.append(song)
    t.append(int(time))

x = input()
T = s.index(x)
print(sum(t[T+1:]))
