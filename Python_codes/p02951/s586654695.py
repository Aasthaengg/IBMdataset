a,b,c = map(int, input().split())
k = a - b
if k >= c:
    print(0)
elif k < c:
    print(c-k)