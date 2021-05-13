h,w = map(int,input().split())

a = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
    a[i] = list(input())

#print(a)

for i in range(h):
    for j in range(w):
        if(a[i][j] == "#"):
            continue
        else:
            cnt = 0
            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    if(k == 0 and l == 0):
                        continue
                    else:
                        x = i + k
                        y = j + l 
                        if(0<= x < h and 0<= y < w and a[x][y] == "#"):
                            cnt += 1
            
            a[i][j] = str(cnt)


#print(a)

for i in range(h):
    ans = ''.join(a[i])
    print(ans)
