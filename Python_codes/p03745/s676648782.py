n = int(input())
A = list(map(int, input().split()))
B = []
for a in A:
    if B:
        if B[-1] == a:
            continue
        else:
            B.append(a)
    else:
        B.append(a)

#print(B)
m = len(B)
X = []
for i in range(m):
    if i == 0:
        cur = B[0]
        cnt = 1
        flag = 0
    else:
        if flag == 0:
            if B[i] > cur:
                flag = 1
                cnt += 1
                cur = B[i]
            if B[i] < cur:
                flag = -1
                cnt += 1
                cur = B[i]
        elif flag == 1:
            if B[i] > cur:
                cnt += 1
                cur = B[i]
            else:
                X.append(cnt)
                cur = B[i]
                cnt = 1
                flag = 0
        else:
            if B[i] < cur:
                cnt += 1
                cur = B[i]
            else:
                X.append(cnt)
                cur = B[i]
                cnt = 1
                flag = 0
    #print(i, flag, cnt)
else:
    X.append(cnt)
#print(X)
print(len(X))
