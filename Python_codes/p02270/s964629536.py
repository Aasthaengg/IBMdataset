def can(l, k, p):
    s, a = 0, 0
    for li in l:
        if li > p: return False
        s += li

        if s > p:
            s = li
            k -= 1
        if k <= 0: return False
        
    return True

def bi(array, k, l, r):
    m = (l + r) // 2
    if l > r:
        return max(l, r)
    b = can(array, k, m)
    if b:
        return bi(array, k, l, m-1)
    else:
        return bi(array, k, m+1, r)
        
    
n, k = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())
    
p = sum(l)
print(bi(l, k, 0, p))
