A, B, C, D, E, F = map(int,input().split())

ans = [0, 0, -1]
for a in range(1+F//A):
    for b in range(1+F//B):
        w = 100*A*a + 100*B*b
        if 0 < w < F:
            for c in range(1+(F-w)//C):
                for d in range(1+(F-w)//D):
                    s = C*c + D*d
                    if 0 < w + s <= F and s/w <= E/100:
                        if ans[2] < s/(w+s):
                            ans = [w+s,s,s/(w+s)]
print(*ans[:2])
