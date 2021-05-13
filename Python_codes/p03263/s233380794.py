H,W = list(map(int,input().split()))
A = []
for i in range(H):
    A.append(list(map(int,input().split())))

cnt = 0
ope = []
for i in range(H):
    nowH = i
    for j in range(W):
        if i%2==1:
            nowW = W-1-j
        else:
            nowW = j

        if j==W-1:
            nextH = i+1
            nextW = nowW
        else:
            nextH = nowH
            if i%2==1:
                nextW = nowW-1
            if i%2==0:
                nextW = nowW+1

        if nextH>=H or nextW>=W:
            break

        if A[nowH][nowW]%2==1:
            A[nowH][nowW] += -1
            A[nextH][nextW] += 1
            ope.append([nowH+1,nowW+1,nextH+1,nextW+1])
            cnt+=1

print(cnt)
for i in range(len(ope)):
    print(ope[i][0],ope[i][1],ope[i][2],ope[i][3])
