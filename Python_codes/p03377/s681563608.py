a, b, x = map(int, input().split())

if a <= x:
    if a + b >= x:
        print("YES")
        exit()
print("NO")