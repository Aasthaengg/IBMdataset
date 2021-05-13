S = input()
val = 10**9
 
voc = set(S)
for c in voc:
    cnt = 0
    tmp = list(S)
 
    while True:
        if all([w == c for w in tmp]):
            val = min(cnt, val)
            break
        cnt += 1
        for u in range(len(tmp)-1):
            tmp[u] = c if tmp[u] == c or tmp[u+1] == c else tmp[u]    
        tmp.pop()
 
 
print(val)