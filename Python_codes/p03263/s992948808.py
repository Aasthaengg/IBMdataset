import sys,math,collections,itertools
input = sys.stdin.readline

H,W= list(map(int,input().split()))
a = [ list(map(int,input().split())) for _ in range(H)]
operation = []

#-奇数だったら右へずらしていく。偶数ならなにもしない-#
cnt = 0
for ih in range(H):
    for iw in range(W-1):
        if a[ih][iw]%2 == 0:
            continue
        else:
            a[ih][iw] -= 1
            a[ih][iw+1] += 1
            cnt += 1
            operation.append([ih+1,iw+1,ih+1,iw+2])
#-最右端を上から下まで-#
for ih in range(H-1):
    if a[ih][W-1]%2 == 0:
        continue
    else:
        a[ih][W-1] -= 1
        a[ih+1][W-1] += 1
        cnt += 1
        operation.append([ih+1,W,ih+2,W])
print(cnt)
for ope in operation:
    print(*ope)
