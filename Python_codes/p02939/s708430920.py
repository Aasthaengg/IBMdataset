s = input()
cnt = 1
now = s[0]
index = 1

while True:
    if s[index] == now and index == len(s)-1:
        break
    if s[index] == now:
        now = s[index:index+2]
        index += 2
        cnt += 1
    else:
        now = s[index]
        index += 1
        cnt += 1
    if index >= len(s):
        break

print(cnt)