s = input()
cnt = 0
steps = 0
for i in range(len(s)):
    if s[i] == 'W':
        steps += i - cnt
        cnt += 1
print(steps)