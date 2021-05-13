h,w,k = map(int,input().split())

s = [input() for i in range(h)]

#print(s)

ans = [[0 for i in range(w)]for j in range(h)]

now_h = 0
now_w = 0
num = 1

li = []

for i in range(h):
    now_w = 0
    for j in range(w):
        #print(i,j,now_w)
        if s[i][j] == '#':
            #print(now_h+1>=i,i,j)
            #if now_h+1 >= i:
                #print(now_h==i)
            for k in range(j-now_w+1):
                ans[i][now_w+k] = num
            """
            else:
                for k in range(now_w-j+1):
                    if s[i][k] == 1:
                        a = 1
            """
            now_h = i
            now_w = j+1
            num += 1


for i in range(h):
    for j in range(w):
        if ans[i][j] == 0:
            ans[i][j] = ans[i][j-1]


for i in range(h):
    for j in range(w):
        if ans[i][j] == 0:
            flag = False
            for k in range(h):
                if i+1+k >= h:
                    break
                if ans[i+1+k][j] != 0:
                    ans[i][j] = ans[i+1+k][j]
                    flag = True
                    break
            if flag == False:
                for k in range(h):
                    if i-1-k < 0:
                        break
                    if ans[i-1-k][j] != 0:
                        ans[i][j] = ans[i-1-k][j]
                        break

for i in range(h):
    print(*ans[i])