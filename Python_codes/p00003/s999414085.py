a = int(input())
for _ in range(a):
    b, c, d = sorted(map(int, input().split()))
    if b**2+c**2 == d**2:
        print("YES")
    else:
        print("NO")