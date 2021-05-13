s = input()
cnt = [0]*26
ans = ""
if s[0] == "z":
    print(-1)
    exit(0)
for i in range(len(s)):
    if cnt[int(ord(s[i])-ord("a"))] == 1:
        min = chr(ord("z")+1)
        for j in range(26):
            if cnt[j] == 0:
                if int(ord(s[i])) < ord(chr(j+ord("a"))) < ord(min):
                    min = chr(j+ord("a"))
        ans += min
        print(ans)
        exit(0)
    else :
        ans += s[i]
        cnt[int(ord(s[i])-ord("a"))] = 1
if ans == s :
    min = chr(ord("z") + 1)
    for j in range(26):
        if cnt[j] == 0:
            if ord(chr(j+ord("a"))) < ord(min):
                min = chr(j+ord("a"))
    if min == chr(ord("z") + 1):
        if s[0] == "z":
            print(-1)
            exit(0)
        else:
            for k in range(len(s)-1,-1,-1):
                ans = ans.strip(s[k])
                cnt[int(ord(s[k])-ord("a"))] -= 1
                if ord(s[k]) > ord(s[k-1]):
                    ans = ans.strip(s[k-1])
                    min = chr(ord("z") + 1)
                    for j in range(26):
                        if cnt[j] == 0:
                            if int(ord(s[k-1])) < ord(chr(j + ord("a"))) < ord(min):
                                min = chr(j + ord("a"))
                    ans += min
                    break
    else:
        ans += min
print(ans)
