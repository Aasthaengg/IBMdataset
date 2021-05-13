h,w = list(map(int,input().split()))
l = [list(input()) for i in range(h)]

x = [1,-1,1,-1,0,0,1,-1]
y = [1,-1,0,0,1,-1,-1,1]
n_s = []
for i in range(h):
    n_l = []
    for j in range(w):
        cnt=0
        for k in range(8):
            if l[i][j]=="#":
                cnt = "#"
                break
            elif 0<=i+x[k]<h and 0<=j+y[k]<w:
                if l[i+x[k]][j+y[k]]=="#":
                    cnt+=1
            else:
                continue
        n_l.append(str(cnt))
    n_s.append(n_l)

for i in n_s:
    print("".join(i))


