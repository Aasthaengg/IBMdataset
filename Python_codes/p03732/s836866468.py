from operator import itemgetter

N,W = map(int, input().split())
List = [[int(l) for l in input().split()] for _ in range(N)]

num = [0]*4
w0 = List[0][0]
for i in range(N):
    num[List[i][0]-w0] += 1
    
List.sort(reverse=True, key=itemgetter(1))
L = []
for i in range(N):
    if List[i][0] == w0:
        L.append(List[i])
for i in range(N):
    if List[i][0] == w0+1:
        L.append(List[i])
for i in range(N):
    if List[i][0] == w0+2:
        L.append(List[i])
for i in range(N):
    if List[i][0] == w0+3:
        L.append(List[i])
        
prev = w0
for i in range(1, N):
    if L[i][0] == prev:
        L[i][1] += L[i-1][1]
    else:
        prev += 1
        
ans = 0
for i in range(-1, num[0]):
    wi = (i+1)*w0
    ci = 0
    if i >= 0:
        if wi > W:
            break
        ci += L[i][1]
    for j in range(-1, num[1]):
        wj = (j+1)*(w0+1)
        cj = 0
        if j >= 0:
            if wi+wj > W:
                break
            cj += L[j+num[0]][1]
        for k in range(-1, num[2]):
            wk = (k+1)*(w0+2)
            ck = 0
            if k >= 0:
                if wi+wj+wk > W:
                    break
                ck += L[k+num[0]+num[1]][1]
            for l in range(-1, num[3]):
                wl = (l+1)*(w0+3)
                cl = 0
                if l >= 0:
                    if wi+wj+wk+wl > W:
                        break
                    cl += L[l+num[0]+num[1]+num[2]][1]
                ans = max(ans, ci+cj+ck+cl)
            
print(ans)