N = int(input())
a = [int(input()) for _ in range(N)]

odd = len([ai for ai in a if ai%2==1])

if odd > 0:
    print("first")
else:
    print("second")
