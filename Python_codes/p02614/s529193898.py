h,w,k = map(int,input().split())

box, ans = [], 0

for i in range(h):
    box.append(input())


for i in range(1 << h):
    for j in range(1 << w):
        count = 0
    
        for H in range(h):
            if i >> H & 1:
                continue
            
            for W in range(w):
                if j >> W & 1:
                    continue
                
                if box[H][W] == '#':
                    count += 1
            
        if count == k:
            ans += 1

print(ans)