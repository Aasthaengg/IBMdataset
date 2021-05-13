n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    if a == "insert":
        d[b] = 1
    else:
        print("yes" if b in d else "no")
