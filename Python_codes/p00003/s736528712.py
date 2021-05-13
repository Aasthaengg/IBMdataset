N = int(input())
for _ in range(N):
    a, b, c = sorted(list(map(int, input().split())))
    print("YES" if a*a + b*b == c*c else "NO")