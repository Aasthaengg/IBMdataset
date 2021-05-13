#2019/10/03
a, b, c = map(int, open(0).read().split())
print("YES" if (b-a) == (c-b) else "NO")