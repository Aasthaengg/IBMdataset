a,b,c,k = map(int, input().split())
l = 0

if a >= k:
    print(k)

else:
    l = a
    k -= a
    
    if b >= k:
        print(l)
        
    else:
        k -= b
        print(l-k)