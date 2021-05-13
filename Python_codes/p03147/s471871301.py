N = int(input())
H = list(map(int,input().split()))
H.append(0)

cnt = 0
stop = max(H)
while stop>0:
    stop += -1
    for i in range(N):
        if H[i]>0 and H[i+1]==0:
            cnt+=1
    for i in range(N):
        if H[i]>0:
            H[i]+=-1
print(cnt)
