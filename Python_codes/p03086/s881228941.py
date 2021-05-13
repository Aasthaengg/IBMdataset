s = input()
l = ['A', 'C', 'G', 'T']

ans = 0
now = 0
for i in s:
    if i in l:
        now += 1
        if now > ans:
            ans = now
    else:
        now = 0

print(ans)