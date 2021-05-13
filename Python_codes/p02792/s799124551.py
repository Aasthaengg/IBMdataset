mod = 1e9+7
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    m = {}
    N = int(raw_input())
    
    for i in range(1, N+1):
        s = str(i)
        first = s[0]
        last = s[-1]
        key = first + last
        m[key] = m.get(key, 0) + 1
    
    ans = 0
    
    #print(m)
    for k in m:
        if k[0] == k[1]:
            ans += m[k] * m[k]
        else:
            swap = k[1] + k[0]
            ans += m[k] * m.get(swap, 0)
    """
    for key1 in m:
        for key2 in m:
            #if key1 == key2:
            #    continue
            if key1[0] == key2[1] and key1[1] == key2[0]:
                ans += m[key1] * m[key2]
    """
    
    print(ans)
    
    
    

main()