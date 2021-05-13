#coding:utf-8
   
n, k = map(int, input().split())
backList = []
for i in range(n):
    backList.append(int(input()))

def capa(p,k):
    cnt = 0
    pcopy = p
    num = 0
    for back in backList:
        if back > p:
            break
        if back <= pcopy:
            pcopy -= back
            cnt += 1
            continue
        elif back > pcopy:
            if num == k-1:
                return cnt
            pcopy = p - back
            cnt += 1
            num += 1          
    return cnt


p_min = 0
p_max = 100000 * 10000
def biSearch(p_min, p_max):
    p = p_max - p_min
    if p_max - p_min <= 1:
        return p_max
    if p % 2 == 0:
        c = p_min + int(p/2)
    else:
        c = p_min + int((p+1)/2)
    v = capa(c,k)
    if v < n:
        p_min = c
    else:
        p_max = c

    return biSearch(p_min, p_max)
            

p = biSearch(p_min, p_max)
n_init = n
while n_init <= n:
    p -= 1
    n = capa(p,k)

print(p+1)

