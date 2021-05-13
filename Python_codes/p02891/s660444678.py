import sys

s = input()
k = int(input())

flg = True
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        flg = False
        break

if flg:
    print(len(s) * k // 2)
    sys.exit()

ans = 0
skip = -1
for i in range(len(s) - 1):
    if i == skip:
        continue
    
    if s[i] == s[i + 1]:
        ans += 1
        skip = i + 1
        
#print(ans)
ans *= k


if s[0] == s[-1]:
    cnt_h = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            cnt_h += 1
        else:
            break
    
    cnt_t = 1
    for i in reversed(range(1, len(s))):
        if s[i] == s[i - 1]:
            cnt_t += 1
        else:
            break
    #print(cnt_h, cnt_t)
    cnt = cnt_h // 2 + cnt_t // 2
    cnt -= (cnt_h + cnt_t) // 2
    cnt *= k - 1
    ans -= cnt

print(ans)