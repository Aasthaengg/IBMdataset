s = input()

l = len(s)
ans = 0

for i in range(1 if l % 2 else 2, l, 2):
    t = s[:-i]
    tl = (l-i)//2

    if t[:tl] == t[tl:]:
        ans = tl*2
        break


print(ans)
