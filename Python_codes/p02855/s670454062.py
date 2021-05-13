h, w, k = map(int, input().split())

s = [list(input()) for _ in range(h)]

c = [-1] * h
for i, r in enumerate(s):
    c[i] = r.count('#')
 
ans = [[-1] * w for _ in range(h)]
first_flag = False
z = []
a = 0
for i in range(h):
    if c[i] == 0:
        if first_flag == False:
            z.append(i)
        else:
            ans[i] = ans[i-1]
    else:
        a += 1
        cnt = 0
        for j in range(w):
            if s[i][j] == "#":
                first_flag = True
                if cnt == 0:
                    cnt += 1
                else:
                    cnt += 1
                    a += 1
            ans[i][j] = a

for i in z[::-1]:
    ans[i] = ans[i+1]
        

for i in range(h):
    print(*ans[i])