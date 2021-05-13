S = input()

ans = 0
cnt = 0

for topcodeer in S :
    if topcodeer == "g" :
        if cnt > 0 :
            cnt -= 1
            ans += 1
        else :
            cnt += 1
    else :
        if cnt > 0 :
            cnt -= 1
        else :
            cnt += 1
            ans -= 1

print(ans)
