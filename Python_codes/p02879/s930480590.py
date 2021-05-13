
a, b = map(int, input().split())

count = (1,2,3,4,5,6,7,8,9)

if a not in count or b not in count:
    print(-1)
else:
    print(a * b)

