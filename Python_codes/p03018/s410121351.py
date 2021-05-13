s = input()
pos = 0
cnt = 0
acnt = 0
if len(s) < 3:
    print(0)
else:
    while(True):
        if s[pos:pos+2] == "BC" and acnt > 0:
            pos += 2
            cnt += acnt
            # print(s, s[pos:pos+2], cnt, pos)
        else:
            if s[pos] == "A":
                acnt += 1
            else:
                acnt = 0
            pos += 1
        if pos >= len(s)-1:
            break
    print(cnt)

