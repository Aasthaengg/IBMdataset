N = int(input())
X = [[int(_) for _ in input().split()] for _ in range(N)]

X.sort(key=lambda x: x[1])

t = 0
for a, b in X:
    t += a
    if t > b:
        print("No")
        exit(0)
print("Yes")
