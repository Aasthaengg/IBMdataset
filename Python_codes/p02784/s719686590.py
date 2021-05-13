h, n = map(int, input().split())
a = list(map(int, input().split()))

result = sum(a)

if h - result <= 0:
    print("Yes")
else:
    print("No")
