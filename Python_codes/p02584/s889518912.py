x,k,d = map(int,input().split(' '))
a = abs(x) % d 
b = -(a - d)
if abs(x) // d > k:
    ans = abs(x) - k * d
else:
    if a == b:
        ans = a
    else:
        if a < b:
            n1 = a
            n2 = b
        if b < a:
            n1 = b
            n2 = a
        if k % 2 == (abs(x) // d) % 2:
            ans = a
        else:
            ans = b
print(ans)