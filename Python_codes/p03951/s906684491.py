N = int(input())
s = input()
t = input()

dupe = 0
for i in range(N):
    for j in range(N + 1):
        if s[i:] == t[:j]:
            dupe = max(dupe, len(s[i:]))
print(N * 2 - dupe)

