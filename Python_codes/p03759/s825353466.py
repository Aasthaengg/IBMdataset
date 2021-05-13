A, B, C = map(int, input().split())

BA = B-A
CB = C-B

if BA == CB:
    print("YES")
else:
    print("NO")
