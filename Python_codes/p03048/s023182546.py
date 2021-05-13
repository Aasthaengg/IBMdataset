#19 B - RGB Boxes
R,G,B,N = map(int,input().split())
lis = sorted([R,G,B])
MA, MID, MI = lis[0],lis[1],lis[2]

cnt = 0
for ma in range(N//MA+1):
    for mid in range(N//MID+1):
        mi = (N - (MA*ma+MID*mid))//MI
        mi_judge = (N - (MA*ma+MID*mid))%MI
        if mi>= 0 and (mi_judge == 0):
            cnt += 1
print(cnt)