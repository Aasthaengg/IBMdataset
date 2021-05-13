a,b,c,d,e,f = map(int, input().split())

per = 0.0
ans = salt = w = s = 0
for i in range(0, f + 1, 100 * a):
    for j in range(0, f + 1, 100 * b):
        w = i + j
        if w > f: break
        for k in range(0, f + 1, c):
            if w + k > f: break
            for l in range(0, f + 1, d):
                w = i + j
                s = k + l
                if w + s > f: break
                if s <= (w // 100) * e:
                    if 0 < s + w <= f:
                        if per < s / (s + w):
                            per = s / (s + w)
                            ans = w + s
                            salt = s
if ans == 0:
    print(100*a,0)
else:
    print(ans,salt)