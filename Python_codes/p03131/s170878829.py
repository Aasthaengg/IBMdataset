k, a, b = map(int, input().split())

if b-a <= 1:
    print(k+1)
else:
    if k <= a-1:
        print(1+k)
    elif k == a:
        print(1+k)
    else:
        k -= a-1
        print(b + ((k-2)//2)*(b-a) + k % 2)
