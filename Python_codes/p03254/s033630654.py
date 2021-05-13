n,x = map(int,input().split())
s = sorted(list(map(int,input().split())))
cnt = 0
for i in range(len(s)):
    if(x - s[i] >= 0 ):
        if(x < s[i] or (i == len(s)-1 and x != s[i])):
            break
        else:
            cnt += 1
        x = x-s[i]
print(cnt)