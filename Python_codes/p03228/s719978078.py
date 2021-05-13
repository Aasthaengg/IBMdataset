a, b, k = map(int, input().split())
for i in range(k):
    if i%2 is 0:
        if a%2 is 1:
            a = (a-1)//2
            b += a
        else:
            a //= 2
            b += a
    
    elif i%2 is 1:
        if b%2 is 1:
            b = (b-1)//2
            a += b
        else:
            b //= 2
            a += b
print(a, b)
        
