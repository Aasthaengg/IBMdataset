a, b, c = input().split()
f = lambda x, y, z : x[-1] == y[0] and y[-1] == z[0]
print("YES" if f(a, b, c) else "NO")