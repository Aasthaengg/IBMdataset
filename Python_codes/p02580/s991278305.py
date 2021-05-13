import sys
h,w,m = map(int,input().split())
hight = [0]*h
width = [0]*w
S = set()

for i in range(m):
    hi,wi = map(int,input().split())
    S.add((hi-1,wi-1))
    hight[hi-1] += 1
    width[wi-1] += 1

max_vh = max(hight)
max_vw = max(width)

max_h = [i for i in range(h) if hight[i] == max_vh]
max_w = [i for i in range(w) if width[i] == max_vw]
for i in max_h:
    for j in max_w:
        if not(i,j) in S:
            print(max_vh+max_vw)
            sys.exit()

print(max_vh+max_vw-1)

