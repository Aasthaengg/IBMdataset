H, A = map(int, input().split())

count = H // A
if H % A != 0:
    count += 1

print(count)
