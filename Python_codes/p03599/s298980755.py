a, b, c, d, e, f =map(int, input().split())

ans = 0
ans_ws = 0
ans_s = 0
for i in range(30//a+1):
    for j in range(30//b+1):
        w = 100*a*i+100*b*j
        s_max = f-w
        if s_max < 0:
            continue
        for k in range(s_max//c+1):
            temp = s_max - c*k
            if temp < 0:
                continue
            for l in range(temp//d+1):
                s = c*k + d*l
                if w+s == 0 or w+s > f:
                    continue
                else:
                    if 100*s > e*w:
                        continue
                    else:
                        x = (100*s)/(w+s)
                        if x >= ans:
                            ans = x
                            ans_ws = w+s
                            ans_s = s
print(ans_ws, ans_s)