a = [int(i) for i in input().split()]
k = int(input())
mx = max(a)
sm = (sum(a)-mx) + mx*(2**k)
print(sm)