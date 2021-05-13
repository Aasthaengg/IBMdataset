s = input()
t = input()

sl = len(s)
tl = len(t)

ans = tl

for i in range(sl):
    if i < sl - tl + 1:
        ss = s[i:i+tl]
        num = 0
        for j in range(tl):
            if ss[j] != t[j]:
                num += 1
        if num < ans:
            ans = num

print(ans)
