s = input()
t = input()


max = 0

for offset in range(len(s)-len(t)+1):
    cnt = 0
    for i in range(len(t)):
        if t[i] == s[offset+i]:
            cnt += 1
    if cnt > max:
        max = cnt

print(len(t)-max)