N = int(input())

s = {}

for _ in range(N):
    tmp = input()
    s[tmp] = 1

print(len(s.keys()))