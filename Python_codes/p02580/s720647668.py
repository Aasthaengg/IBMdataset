import sys
H,W,m = map(int, input().split())

high = [0] * H
width = [0] * W

stone = set()
for i in range(m):
    h, w = map(int,input().split())
    h -= 1
    w -= 1
    
    high[h] += 1
    width[w] += 1
    stone.add((h,w))
    
dic_h = {}
for i in range(len(high)):
    dic_h.setdefault(high[i], [])
    
    dic_h[high[i]].append(i)
    
dic_w = {}
for i in range(len(width)):
    dic_w.setdefault(width[i], [])
    
    dic_w[width[i]].append(i)
    
h_max = max(dic_h.keys())
w_max = max(dic_w.keys())

for i in dic_h[h_max]:
    for j in dic_w[w_max]:
        if (i,j) not in stone:
            print(h_max+w_max)
            sys.exit(0)
            
print(h_max+w_max-1)