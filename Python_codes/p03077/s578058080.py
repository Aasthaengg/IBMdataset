n = int(input())
l = [int(input()) for _ in range(5)]

if min(l) >= n:
    print(5)
else:
    print((n-1)//min(l) + 5)