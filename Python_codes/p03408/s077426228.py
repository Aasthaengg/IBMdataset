N = int(input())
words = {}

for _ in range(N):
    s = input()
    if s in words:
        words[s] += 1
    else:
        words[s] = 1

M = int(input())

for _ in range(M):
    t = input()
    if t in words:
        words[t] -= 1

val = sorted(words.values())

if val:
    if val[-1] < 0:
        print(0)
    else:
        print(val[-1])
else:
    print(0)