A, B, C = list(map(int, input().split()))
if (A-B) - C > 0:
    print(0)
else:
    print(C-(A-B))