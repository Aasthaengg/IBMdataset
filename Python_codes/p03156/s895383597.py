n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
small = 0
medium = 0
large = 0
for score in p:
    if score <= a:
        small += 1
    elif a < score <= b:
        medium += 1
    elif score > b:
        large += 1
ans = min(small, medium, large)
print(ans)
