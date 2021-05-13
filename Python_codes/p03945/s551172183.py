l = list(input())
n = len(l)

idx = 0
seg = []
while idx < n:
    while idx < n-1 and l[idx] == l[idx+1]:
        idx+=1
    seg.append(idx)
    idx+=1
print(len(seg)-1)
