# greedyに分割していく
s = input()
bak = ''
buf = ''
ans = []
for i,c in enumerate(s):
    buf += c
    if buf != bak:
        ans.append(buf)
        bak, buf = buf, ''

print(len(ans))