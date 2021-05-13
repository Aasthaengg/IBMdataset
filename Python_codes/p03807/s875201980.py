n = int(input())
a = [int(i) for i in input().split()]

c = 0

for i in a:
    if i % 2 != 0:
        c += 1

print("YES" if c % 2 == 0 else "NO")