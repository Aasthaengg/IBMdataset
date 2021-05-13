n,k = map(int,input().split())
if k == 1 or n - k <= 0:
    print(0)
elif n - k > 0:
    print(n - k)