n = int(input())
a = list(map(int, input().split()))
s = 0
for ai in a:
    s ^= ai
print(*[s ^ ai for ai in a])