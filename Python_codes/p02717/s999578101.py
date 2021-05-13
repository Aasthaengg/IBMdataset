a, b, c = input().split()

a, b = b, a
a, c = c, a

ans = (" ").join([a, b, c])
print(ans)
