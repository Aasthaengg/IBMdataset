n, k, c = map(int, input().split())
s = list(input())

forward = []
backward = []
i = 0
while i < len(s) and len(forward) < k:
    if s[i] == 'x':
        i += 1
        continue
    forward.append(i)
    i += c + 1
i = len(s)-1
while i > -1 and len(backward) < k:
    if s[i] == 'x':
        i -= 1
        continue
    backward.append(i)
    i -= c
    i -= 1

for i in range(len(forward)):
    if forward[i] == backward[len(backward) - i - 1]:
        print(forward[i] + 1)