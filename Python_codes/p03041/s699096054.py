x, y = map(int, input().split())
z = list(input())
z[y-1] = z[y-1].lower()
print("".join(z))

