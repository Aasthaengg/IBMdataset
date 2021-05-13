H,W,N = map(int, input().split())

field = {}
for i in range(N):
    a,b = map(int, input().split())
    a,b = a-1,b-1
    for j in range(a-1, a+2):
        for k in range(b-1, b+2):
            if not j in field:
                field[j] = {}
            if not k in field[j]:
                field[j][k] = 0
            field[j][k] += 1

ans = [0] * 10
for kh in field.keys():
    for kw in field[kh].keys():
        if 1 <= kh <= H-2 and 1 <= kw <= W-2:
            ans[field[kh][kw]] += 1

tmp = (H-2)*(W-2)
for i in range(1,10):
    tmp -= ans[i]

ans[0] = tmp
for i in range(10):
    print(ans[i])

