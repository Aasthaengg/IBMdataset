S = input()
chrs = set(S)

if len(chrs) == 1:
    ans = 0
else:
    ans = len(S)
    for c in chrs:
        cnt = 0
        cur = S
        while True:
            new = ""
            for i in range(len(cur) - 1):
                if cur[i] == c or cur[i + 1] == c:
                    new += c
                else:
                    new += "*"
            cnt += 1
            if len(set(new)) == 1:
                break
            cur = new

        if cnt < ans:
            ans = cnt

print(ans)
