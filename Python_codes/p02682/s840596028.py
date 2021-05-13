a, b, c, k = map(int,input().split())

if k <= a:
    print(k)
elif (k > a) and (k - a <= b):
    print(a)
elif (k > a) and (k - a > b):
    print(a - (k-a-b))
    
