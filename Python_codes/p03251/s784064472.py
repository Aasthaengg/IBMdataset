n, m, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for z in range(x + 1, y + 1):
    if max(a) < z <= min(b):
        print("No War")
        exit()
print("War")
