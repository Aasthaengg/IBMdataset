s = list(input())

ans = 0
while ans == 0:
    cnt = 0
    del s[-1], s[-1]
    for i in range(len(s)//2):
        if s[i] != s[i + len(s)//2]:
            break
        cnt += 1
    if cnt == len(s)//2:
        ans = len(s)

print(ans)