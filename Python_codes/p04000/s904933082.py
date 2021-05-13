from collections import defaultdict
import sys
input = sys.stdin.readline

H,W,N = map(int,input().split())
D = defaultdict(bool)
B = []

for _ in range(N):
    a,b = map(lambda x: int(x)-1,input().split())
    D[(a,b)] = True
    B.append((a,b))

ans = [0 for _ in range(10)]

for a,b in B:
    for i in range(9):
        ix,iy = divmod(i,3)
        if a-ix<0 or b-iy<0:
            continue
        black_count = 0
        for j in range(9):
            jx,jy = divmod(j,3)
            if H<=a-ix+jx or W<=b-iy+jy:
                break
            if (a-ix+jx,b-iy+jy) in D:
                if -iy+jy<0 or (-iy+jy==0 and -ix+jx<0):
                    break
                black_count += 1
        else:
            ans[black_count] += 1

ans[0] = (H-2)*(W-2)-sum(ans)
print(*ans,sep='\n')