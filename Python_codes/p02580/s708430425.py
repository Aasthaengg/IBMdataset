import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0


H,W,M = map(int,readline().split())

col = [0]*W
row = [0]*H
elements = []
for i in range(M):
    h,w = map(int,readline().split())
    h,w = h-1,w-1
    elements.append((h,w))
    col[w] += 1
    row[h] += 1

def rank(lst,syoujun=False):
    res2 = list(set(lst))
    ans = []
    if syoujun:
        res2.sort()
    else:
        res2.sort(reverse=True)
    dic1 = dict()
    for i in range(len(res2)):
        dic1[res2[i]] = i
    for i in lst:
        #ans.append(dic1[i]) #zero-indexed
        ans.append(dic1[i] + 1) #one-indexed
    
    return ans

col2 = rank(col)
row2 = rank(row)

cmax = col2.count(1)
rmax = row2.count(1)

counter = 0
for i,j in elements:
    if col2[j] == 1 and row2[i] == 1:
        counter += 1

if counter == cmax*rmax:
    print(max(col) + max(row)-1)
else:
    print(max(col) + max(row))