H, W, N = map(int, input().split())
d = 10**9+1
L = []
S = set()
for _ in range(N):
    a, b = map(int, input().split())
    S.add((a, b))
Map =[[0]*5 for _ in range(5)]
ans = [0]*10
for i in S:
    a, b = i
    for i in range(-2, 3):
        for j in range(-2, 3):
            a1, b1 = a+i, b+j

            if (1<=a1<=H) and (1<=b1<=W):
                if (a1, b1) in S:
                    Map[i+2][j+2] = 1
                else:
                    Map[i+2][j+2] = 0
            else:
                Map[i+2][j+2] = -100
    for i in range(-1, 2):
        for j in range(-1, 2):
            res = 0
            for k in range(3):
                for l in range(3):
                    res+=Map[i+1+k][j+1+l]
            if res>=0:
                ans[res]+=1
for i in range(1, 10)[::-1]:
    ans[i] //=i
ans[0] = (W-2)*(H-2)-sum(ans)
for i in ans:
    print(i)