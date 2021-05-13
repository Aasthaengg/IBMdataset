def main():
    s = list(map(int,input().strip().split()))
    k = s[3]
    r = 0
    if s[0] <= k:
        r += 1 * s[0]
        k -= s[0]
    else:
        r += 1 * k
        print(r)
        return
    
    if (k-s[1]) <=0:
        print(r)
        return
    
    if s[2] <= (k-s[1]):
        r += (-1)*s[2]
    else:
        r += (-1) * (k-s[1])
    
    print(r)
    return
    
    
main()
