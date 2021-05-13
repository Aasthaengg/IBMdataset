# 135 A

a, b = map(int, input().split())

if a != b:
    if (a + b) % 2 == 0:
        k = (a + b) // 2
        print(k)
    else:
        print("IMPOSSIBLE")
else:
    print(0)