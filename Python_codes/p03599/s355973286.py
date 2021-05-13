import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

A,B,C,D,E,F = MI()

density = 0
ans = (100*A,0)
for i in range(30):  # 操作1の行う回数
    for j in range(30):  # 操作2の行う回数
        if i == 0 and j == 0:
            continue
        elif 100*(A*i+B*j) >= F:
            continue
        else:
            r = min(F-100*(A*i+B*j),E*(A*i+B*j))  # 溶かせる砂糖の上限
            a = r
            for k in range(C):
                s = r-D*k
                if s < 0:
                    break
                else:
                    a = min(a,s % C)
            if density < (r-a)/((r-a)+100*(A*i+B*j)):
                density = (r-a)/((r-a)+100*(A*i+B*j))
                ans = ((r-a)+100*(A*i+B*j),(r-a))

print(*ans)