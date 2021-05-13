N = int(input())
a = map(int, input().split(" "))
ans = 0
for ai in a:
    ans ^= ai
print('Yes' if ans == 0 else 'No')