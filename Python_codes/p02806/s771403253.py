N = int(input())
s = []
t = []

for n in range(N):
    song, time = map(str, input().split())
    s.append(song)
    t.append(int(time))

X = input()
idx = s.index(X)

ans = sum(t[idx+1:])
print(ans)
