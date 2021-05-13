n = int(input())
a = list(map(int, input().split()))
c = 0
for i in a:
    c += i % 2
print("YES" if c % 2 == 0 else "NO")