#098_D
def search_1(x):
    l = set()
    n = len(bin(int(x))) - 2
    for j in range(n):
        if (int(x) >> j) & 1:
            l.add(j)
    return l

n = int(input())
a = [search_1(x) for x in input().split()]
#print(a)

ans = 0
cur = set()
r = 0
for l in range(0, n):
    while r < n and len(cur & a[r]) == 0:
        cur |= a[r]
        r += 1
    #print(l, r)
    ans += r - l 
    
    cur -= a[l]
print(ans)