A, B = map(int, input().split())
if A >= 13:
    print(int(B))
elif A >= 6:
    print(int(B//2))
else:
    print(0)