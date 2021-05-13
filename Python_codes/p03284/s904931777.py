n,k = map(int,input().split())
if n % k == 0:
    print(0)
elif n % k != 0:
    x = (n - 1) / k
    print(int((x + 1) - x)) 