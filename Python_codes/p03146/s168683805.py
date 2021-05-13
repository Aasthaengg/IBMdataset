used = dict()
s = int(input())
cnt = 1
while True:
    if s in used:
        break
    cnt += 1
    used[s] = True
    if s&1==1:
        s = 3 * s + 1
    else:
        s = s//2
print(cnt)