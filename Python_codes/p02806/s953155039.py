N = int(input())
s = [None] * N
t = [None] * N
for i in range(N):
    s[i], t[i] = input().split()
    t[i] = int(t[i])
X = input()
for i in range(N):
    if s[i] == X:
        print(sum(t[i + 1:]))