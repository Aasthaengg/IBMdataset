N = int(input())
s, t = [0 for _ in range(N)], [0 for _ in range(N)]
for i in range(N):
    s[i], t[i] = input().split()
    t[i] = int(t[i])
X = input()

ind = s.index(X)
print(sum(t[ind+1:]))
