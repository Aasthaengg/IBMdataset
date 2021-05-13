n, m, x, y = map(int, input().split())
xi = list(map(int, input().split()))
yi = list(map(int, input().split()))

if max(xi)<min(yi) and x<min(yi)<y:
    print("No War")
else:
    print("War")