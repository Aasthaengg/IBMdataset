a, b = (int(i) for i in input().split())
cnt = 0
for i in range(a, b+1):
    s = str(i)
    bool = True
    for j in range(len(s)//2+1):
        if not s[j] == s[len(s)-1-j]:
            bool = False
            break
    if bool:
        cnt += 1
print(cnt)