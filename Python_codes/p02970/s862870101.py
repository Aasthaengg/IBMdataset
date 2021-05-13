#B
n,d = map(int,input().split())

a = n % (d*2+1)

if a > 0:
    print(n // (d*2+1) + 1)
else:
    print(n // (d*2 + 1))